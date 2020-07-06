import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import re
import sys
import logging
logging.getLogger('tensorflow').disabled = True
import numpy as np
import tensorflow as tf
from models import resnet_v2

# TODO disable tensorflow logs
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

class GeoEmbeddings():
    def __init__(self, model_path='/checkpoints', cnn_input_size=224, use_cpu=True):
        self._cnn_input_size = cnn_input_size
        self._image_path_placeholder = tf.placeholder(tf.string, shape=None)
        self._image_crops, _ = self._img_preprocessing(self._image_path_placeholder)

        # build cnn
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        self._sess = tf.Session(config=config)

        model_file = os.path.join(f'{model_path}/', 'model.ckpt')

        with tf.variable_scope(os.path.basename(model_path)) as scope:
            self._scope = scope

        device = '/cpu:0' if use_cpu else '/gpu:0'

        with tf.variable_scope(self._scope):
            with tf.device(device):
                with tf.contrib.slim.arg_scope(resnet_v2.resnet_arg_scope()):
                    self._net, _ = resnet_v2.resnet_v2_101(self._image_crops, is_training=False)

        var_list = {
            re.sub('^' + self._scope.name + '/', '', x.name)[:-2]: x for x in tf.global_variables(self._scope.name)
        }

        # restore weights
        saver = tf.train.Saver(var_list=var_list)
        saver.restore(self._sess, str(model_file))

    def get_img_embedding(self, image_path):
        # feed forward image in cnn and extract result
        # use the mean for the three crops
        try:
            embedding = self._sess.run([self._net], feed_dict={self._image_path_placeholder: image_path})
            return embedding[0].squeeze().mean(axis=0)
        except Exception as e:
            # print(e)
            # logging.error(f'Cannot create embedding for {image_path}')
            return None

    def _img_preprocessing(self, img_path):
        # read image
        img = tf.io.read_file(img_path)

        # decode image
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, dtype=tf.float32)
        img.set_shape([None, None, 3])

        # normalize image to -1 .. 1
        img = tf.subtract(img, 0.5)
        img = tf.multiply(img, 2.0)

        # get multicrops depending on the image orientation
        height = tf.to_float(tf.shape(img)[0])
        width = tf.to_float(tf.shape(img)[1])

        # get minimum and maximum coordinate
        max_side_len = tf.maximum(width, height)
        min_side_len = tf.minimum(width, height)
        is_w, is_h = tf.cond(tf.less(width, height), lambda: (0, 1), lambda: (1, 0))

        # resize image
        ratio = self._cnn_input_size / min_side_len
        offset = (tf.to_int32(max_side_len * ratio + 0.5) - self._cnn_input_size) // 2
        img = tf.image.resize_images(img, size=[tf.to_int32(height * ratio + 0.5), tf.to_int32(width * ratio + 0.5)])

        # get crops according to image orientation
        img_array = []
        bboxes = []

        for i in range(3):
            bbox = [
                i * is_h * offset, i * is_w * offset,
                tf.constant(self._cnn_input_size),
                tf.constant(self._cnn_input_size)
            ]

            img_crop = tf.image.crop_to_bounding_box(img, bbox[0], bbox[1], bbox[2], bbox[3])
            img_crop = tf.expand_dims(img_crop, 0)

            img_array.append(img_crop)
            bboxes.append(bbox)

        return tf.concat(img_array, axis=0), bboxes