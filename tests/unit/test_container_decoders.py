#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from omero_marshal import get_encoder, get_decoder


class TestProjectDecoder(object):

    def assert_project(self, project):
        assert project.name.val == 'the_name'
        assert project.description.val == 'the_description'

    def test_project_decoder(self, project):
        encoder = get_encoder(project.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project)
        v = decoder.decode(v)
        self.assert_project(v)
        assert v.sizeOfDatasetLinks() == 0

    def test_project_with_datasets_decoder(self, project_with_datasets):
        encoder = get_encoder(project_with_datasets.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project_with_datasets)
        v = decoder.decode(v)
        assert v.id.val == 1L
        assert v.name.val == 'the_name'
        assert v.description.val == 'the_description'
        assert v.sizeOfDatasetLinks() == 2
        dataset_1, dataset_2 = v.linkedDatasetList()
        assert dataset_1.id.val == 1L
        assert dataset_1.name.val == 'dataset_name_1'
        assert dataset_1.description.val == 'dataset_description_1'
        assert dataset_2.id.val == 2L
        assert dataset_2.name.val == 'dataset_name_2'
        assert dataset_2.description.val == 'dataset_description_2'

    def test_project_with_datasets_and_images_decoder(
            self, project_with_datasets_and_images):
        encoder = get_encoder(project_with_datasets_and_images.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project_with_datasets_and_images)
        v = decoder.decode(v)
        assert v.id.val == 1L
        assert v.name.val == 'the_name'
        assert v.description.val == 'the_description'
        assert v.sizeOfDatasetLinks() == 2

        dataset_1, dataset_2 = v.linkedDatasetList()

        assert dataset_1.id.val == 1L
        assert dataset_1.name.val == 'dataset_name_1'
        assert dataset_1.description.val == 'dataset_description_1'
        image_1, image_2 = dataset_1.linkedImageList()
        assert image_1.id.val == 1L
        assert image_1.acquisitionDate.val == 1L
        assert image_1.archived.val is False
        assert image_1.description.val == 'image_description_1'
        assert image_1.name.val == 'image_name_1'
        assert image_1.partial.val is False
        assert image_1.format.id.val == 1L
        assert image_1.format.value.val == 'PNG'
        assert image_2.id.val == 2L
        assert image_2.acquisitionDate.val == 1L
        assert image_2.archived.val is False
        assert image_2.description.val == 'image_description_2'
        assert image_2.name.val == 'image_name_2'
        assert image_2.partial.val is False
        assert image_2.format.id.val == 1L
        assert image_2.format.value.val == 'PNG'

        assert dataset_2.id.val == 2L
        assert dataset_2.name.val == 'dataset_name_2'
        assert dataset_2.description.val == 'dataset_description_2'
        image_3, image_4 = dataset_2.linkedImageList()
        assert image_3.id.val == 3L
        assert image_3.acquisitionDate.val == 1L
        assert image_3.archived.val is False
        assert image_3.description.val == 'image_description_3'
        assert image_3.name.val == 'image_name_3'
        assert image_3.partial.val is False
        assert image_3.format.id.val == 1L
        assert image_3.format.value.val == 'PNG'
        assert image_4.id.val == 4L
        assert image_4.acquisitionDate.val == 1L
        assert image_4.archived.val is False
        assert image_4.description.val == 'image_description_4'
        assert image_4.name.val == 'image_name_4'
        assert image_4.partial.val is False
        assert image_4.format.id.val == 1L
        assert image_4.format.value.val == 'PNG'
