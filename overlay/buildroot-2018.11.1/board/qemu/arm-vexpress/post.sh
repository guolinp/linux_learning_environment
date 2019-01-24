#!/bin/sh


echo "Create uboot SD image..."
mkdir -p output/build/uboot_sd_image && \
         output/build/host-genext2fs-1.4.1/genext2fs \
         -b 204800 \
         -d output/images \
         output/build/uboot_sd_image/uboot_sd.image
