##########################################################################
#
#  THIS FILE IS GENERATED FROM TEMPLATE. DON'T MODIFY IT
#
#  uniee_values.py
#
#  Created on: Jan 14, 2022
#      Author: Miroslav Ondra <ondra@faster.cz>
# 


class Product:
	def __init__(self, id, name, **kwargs):
		self.id = id
		self.name = name
		self.vars = kwargs

class Board:
	def __init__(self, id, name, slots, **kwargs):
		self.id = id
		self.name = name
		self.slots = slots
		self.vars = kwargs

class Slot:
	def __init__(self, slot, **kwargs):
		self.slot = slot
		self.vars = kwargs

products = {
  '259': Product(259, 'S103', dt='unipi_s103' , udev='s103' , has_ds2482='1' ),
  '515': Product(515, 'M103', dt='unipi_m103' , udev='m103' , has_ds2482='1' ),
  '771': Product(771, 'M203', dt='unipi_m203' , udev='m203' , has_ds2482='1' ),
  '1027': Product(1027, 'M303', dt='unipi_m303' , udev='m303' , has_ds2482='1' ),
  '1283': Product(1283, 'M523', dt='unipi_m523' , udev='m523' , has_ds2482='1' ),
  '1539': Product(1539, 'L203', dt='unipi_l203' , udev='l203' , has_ds2482='1' ),
  '1795': Product(1795, 'L403', dt='unipi_l403' , udev='l403' , has_ds2482='1' ),
  '2051': Product(2051, 'L523', dt='unipi_l523' , udev='l523' , has_ds2482='1' ),
  '2307': Product(2307, 'L533', dt='unipi_l533' , udev='l533' , has_ds2482='1' ),
  '2563': Product(2563, 'S103_G', dt='unipi_s103_g' , udev='s103_g' , has_ds2482='1' , has_gprs='1' ),
  '2819': Product(2819, 'M403', dt='unipi_m403' , udev='m403' , has_ds2482='1' ),
  '3075': Product(3075, 'M503', dt='unipi_m503' , udev='m503' , has_ds2482='1' ),
  '3587': Product(3587, 'L303', dt='unipi_l303' , udev='l303' , has_ds2482='1' ),
  '3843': Product(3843, 'L503', dt='unipi_l503' , udev='l503' , has_ds2482='1' ),
  '4099': Product(4099, 'L513', dt='unipi_l513' , udev='l513' , has_ds2482='1' ),
  '4355': Product(4355, 'S103_E', dt='unipi_s103_e' , udev='s103_e' , has_ds2482='1' , has_enocean='1' ),
  '4611': Product(4611, 'S103_I', dt='unipi_s103_i' , udev='s103_i' , has_ds2482='1' , has_iqrf='1' ),
  '262': Product(262, 'AKUSO1', dt='unipi_akuso1' , udev='akuso1' , has_watchdog1='1' ),
}

boards = {
  '4': Board(4, 'B_1000_1', None),
  '5': Board(5, 'B_1000_2', None),
  '6': Board(6, 'B_1000_3', None),
}

# Family names
family = {
  '1': 'UNIPI1',
  '2': 'G1XX',
  '3': 'NEURON',
  '5': 'AXON',
  '6': 'CM40',
  '7': 'PATRON',
  '15': 'IRIS',
  '16': 'OEM',
}

def unipi_product_info(product_id, version=None):
	''' return product_info or none '''
	return products.get(str(product_id), None)

def unipi_product_info_by_name(product_name, version=None):
	''' return product_info or none '''
	for k,v in products.items():
		if v.name.lower() == product_name.lower(): 
			return v
		if v.name.lower() == product_name.lower().replace('-','_'):
			return v
	short_name = product_name.lower()
	compare_len = len(short_name) - 1;
	while compare_len > 3:
		for k,v in products.items():
			if v.name.lower()[:compare_len] == short_name[:compare_len]: 
				return v
		compare_len -= 1

	return None

def unipi_board_info(board_id, slot=None, version=None):
	''' return board_info or None '''
	board_info = boards.get(str(board_id), None)
	if slot == None or board_info == None:
		return board_info
	if board_info.slots is None:
		return None
	return board_info.slots.get(str(slot), None)


def unipi_family_name(product_id):
	''' return family name or none '''
	return family.get(str(product_id & 0xff), None)
