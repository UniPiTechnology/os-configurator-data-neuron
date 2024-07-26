INSTALL = install

.PHONY: all

#LINUX_BUILD_PATH = /lib/modules/$(shell uname -r)/build
INSTALL = install
PWD = $(shell pwd)
OVERLAY_DEST_DIR = /boot/overlays
UDEV_DEST_DIR = /opt/unipi/os-configurator/udev
LIB_DEST_DIR = /opt/unipi/os-configurator

ifeq ($(LINUX_BUILD_PATH),)
all:
	MAKEFLAGS="$(MAKEFLAGS)" $(MAKE) -C $(PWD)/overlays overlays
else
all:
	MAKEFLAGS="$(MAKEFLAGS)" $(MAKE) -C $(LINUX_BUILD_PATH) M=$(PWD)/overlays
endif

install: install-overlays install-udev unipi_values.py
	$(INSTALL) -m 644 unipi_values.py $(DESTDIR)/$(LIB_DEST_DIR)
	cp -r files/* $(DESTDIR)

install-overlays: $(wildcard overlays/*.dtbo)
	mkdir -p $(DESTDIR)/$(OVERLAY_DEST_DIR)
	$(INSTALL) -m 644 $^ $(DESTDIR)/$(OVERLAY_DEST_DIR)

install-udev: $(wildcard udev/*.rules)
	mkdir -p $(DESTDIR)/$(UDEV_DEST_DIR)
	[ -z "$^" ] || $(INSTALL) -m 644 $^ $(DESTDIR)/$(UDEV_DEST_DIR)

clean:
	@find overlays \( -name .\*.cmd -o -name .\*.tmp -o -name \*.dtbo \
	      -o -name Module.symvers -o -name modules.order  \) \
	      -delete
