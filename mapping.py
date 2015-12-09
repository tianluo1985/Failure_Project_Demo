

maps={'08':0,
	 '11':1,
	 '12':2,
	 '13':3,
	 '14':4,
	 '15':5,
	 '16':6,
	 '17':7,
	 '19':8,
	 '20':9,
	 '21':10,
	 '23':11,
	 '24':12,
	 '25':13,
	 '26':14,
	 '27':15,
	 '28':16,
	 '29':17,
	 '33':18,
	 '34':19,
	 '341':20,
	 '49':21,
	 '51':22,
	 '58':23,
	 '68':24,
	 '700':25,
	 '72':26,
	 '73':27,
	 '800':28}

desc_maps={'08':'ASIC (Application-Specific INtegrated circuit)',
	 '11':'Capacitors',
	 '12':'Resistors',
	 '13':'Diodes',
	 '14':'Resistor Networks',
	 '15':' MPU (Memory Protection Unit),DRAM (Dynamic Random Addressable Memory),DIMM (Dual In-line Memory Module),DDR ...',
	 '16':'PLD (Programmable Logic Device),FPGA (Field Programmable Gate Array),EPROM (Erasable Programmable Read Only Memory),Flash Memory,SSD ( Solid State Disk)',
	 '17':'Programmed PLD/ Programmed Flash',
	 '19':'Crystals/ Oscillators',
	 '20':'Transistor',
	 '21':'Circuit Protection and Filter',
	 '23':'Relays',
	 '24':'Magnetic/Inductors/toroids/transformers',
	 '25':'LED',
	 '26':'Sockets',
	 '27':'Receptacle/Headers',
	 '28':'PCB (Printed Wire Board)',
	 '29':'Connectors',
	 '33':'Fafns and Blowers',
	 '34':'Power Supplies',
	 '341':'Off-line Front End AC/DC',
	 '49':'Nuts Washers',
	 '51':'Heat Sink',
	 '58':'Hard Disk Drive',
	 '68':'',
	 '700':'',
	 '72':'',
	 '73':'',
	 '800':''}

reverse_map={y:x for x,y in maps.iteritems()}

demo_list=[0,1,2,3,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28]

demo_dict={}
for i in demo_list:
    demo_dict[i]='Component '+reverse_map[i]+': '+desc_maps[reverse_map[i]]
