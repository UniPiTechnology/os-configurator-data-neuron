
dtss += unipi_rtc-overlay.dts
dtss += unipi_id-overlay.dts
dtss += ds2482-overlay.dts

dtss += unipi_s103-overlay.dts
dtss += unipi_m103-overlay.dts
dtss += unipi_m203-overlay.dts
dtss += unipi_m303-overlay.dts
dtss += unipi_m523-overlay.dts
dtss += unipi_l203-overlay.dts
dtss += unipi_l403-overlay.dts
dtss += unipi_l523-overlay.dts
dtss += unipi_l533-overlay.dts
dtss += unipi_s103_g-overlay.dts
dtss += unipi_m403-overlay.dts
dtss += unipi_m503-overlay.dts
dtss += unipi_l303-overlay.dts
dtss += unipi_l503-overlay.dts
dtss += unipi_l513-overlay.dts
dtss += unipi_s103_e-overlay.dts
dtss += unipi_s103_i-overlay.dts
dtss += unipi_akuso1-overlay.dts


dtbo-y = $(dtss:-overlay.dts=.dtbo)
targets  += $(dtbo-y)
always-y += $(dtbo-y)

%.dtbo: %-overlay.dts
	dtc -@ -O dtb -o $@ $<

overlays: $(targets)

.PHONY: overlays