#!/usr/bin/python

import time
import os

def edit_line_file(filename, old_line, new_line):
	print "    Editing", filename
	time.sleep(1)
	file = open(filename, "r")
	lines = []
	for line in file:
		lines.append(line)
	file.close()
	done = False
	for i in range(0, len(lines)):
		#print lines[i]
		if old_line in lines[i]:
			print '    Found "' + old_line + '":      ', lines[i],
			time.sleep(0.5)
			if lines[i].strip('\n') == new_line:
				print "    Already set, skiping..."
				time.sleep(1)
				return 0
			print '    Change to', new_line
			time.sleep(0.5)
			lines[i] = new_line
			done = True

	print "    Search finished."

	if not done:
		print "    Could not find", old_line
		time.sleep(1)
		print "    Adding", new_line, "automaticly"
		time.sleep(1)
		lines.append('\n'+new_line+'\n')
		print "    Finished."
		time.sleep(1)
	print "    Preparing new file"
	new_file = "".join(lines)

	input_incorrect = True
	while input_incorrect:
		message = "    Are you sure to change the file(%s) with new line? (y/n): " % filename
		value = raw_input(message)
		if value in ["n", "N"]:
			print "    The screen will not work, but OK."
			input_incorrect = False
			time.sleep(1)
			print "\n    And I assume you don't wanna go any further, so Bye~"
			quit()
		elif value in ["y", "Y"]:
			print "    Yes, it is!"
			time.sleep(1)
			'''
			print "    Backup..."
			cmd = "cp %s %s.bak" % (filename, filename)
			os.system(cmd)
			time.sleep(1)
			'''
			print "    Write file..."
			file = open(filename, "w")
			file.write(new_file)
			file.close()
			print "   ", filename, "modified to:"
			cmd = "cat " + filename
			os.system(cmd)
			input_incorrect = False
		else:
			print '    Input Error, please input "y", or "n". Try again or Ctrl + C to Exit.'

def edit_cmdline():
	print "    Editing /boot/cmdline.txt"
	time.sleep(1)
	file = open("/boot/cmdline.txt", "r")
	line = file.read()
	file.close()
	map_done = False
	font_done = False
	blocks = line.split(" ")

	for i in range(0, len(blocks)):
		print blocks[i]
		if "fbcon=map:" in blocks[i]:
			print "    Found fbcon=map:    ", blocks[i]
			time.sleep(0.5)
			if blocks[i] == "fbcon=map:10":
				print "    Already set, skiping..."
				time.sleep(1)
				return 0
			print '    Change to "fbcon=map:10"'
			time.sleep(0.5)
			blocks[i] = "fbcon=map:10"
			map_done = True

		if "fbcon=font:" in blocks[i]:
			print "    Found fbcon=font:    ", blocks[i]
			time.sleep(0.5)
			if blocks[i] == "fbcon=font:VGA8x8":
				print "    Already set, skiping..."
				time.sleep(1)
				return 0
			print '    Change to "fbcon=font:VGA8x8"'
			time.sleep(0.5)
			blocks[i] = "fbcon=font:VGA8x8"
			font_done = True

	print "    Search finished."
	if not map_done:
		print "    Could not find fbocn map settings."
		time.sleep(1)
		print "    Adding fbcon=map:10 automaticly"
		time.sleep(1)
		blocks[-1] = blocks[-1].strip('\n')
		blocks.append("fbcon=map:10")
		print "    Finished."
		time.sleep(1)
	if not font_done:
		print "    Could not find fbocn font settings."
		time.sleep(1)
		print "    Adding fbcon=font:VGA8x8 automaticly"
		time.sleep(1)
		blocks[-1] = blocks[-1].strip('\n')
		blocks.append("fbcon=font:VGA8x8")
		print "    Finished."
		time.sleep(1)

	print "\n    Old line:"
	print "     ", line
	time.sleep(1)
	print "\n    New line:"
	new_line = " ".join(blocks)
	print "     ", new_line
	time.sleep(1)

	input_incorrect = True
	while input_incorrect:
		value = raw_input("    Are you sure to change the file with new line? (y/n): ")
		if value in ["n", "N"]:
			print "    The screen will not work, but OK."
			input_incorrect = False
			time.sleep(1)
			print "\n    And I assume you don't wanna go any further, so Bye~"
			quit()
		elif value in ["y", "Y"]:
			print "    Yes, it is!"
			time.sleep(1)
			file = open("/boot/cmdline.txt", "w")
			line = file.write(new_line)
			file.close()
			print "    /boot/cmdline.txt modified to:"
			os.system("cat /boot/cmdline.txt")
			input_incorrect = False
		else:
			print '    Input Error, please input "y", or "n". Try again or Ctrl + C to Exit.'

def main():
	print '==========================================='
	print ""
	print "         2.2 Inch TFT Screen Setup  "
	print ""
	print "                SunFounder"
	print ""
	print "                    support@sunfounder.com"
	print "==========================================="

	print "Setting up for PiTFT..."
	time.sleep(2)


	print "\n\nEnable I2C and SPI:"
	time.sleep(1)

	edit_line_file('/boot/config.txt', 'dtparam=i2c_arm=', 'dtparam=i2c_arm=on')
	print "    I2C enabled."
	time.sleep(1)

	edit_line_file('/boot/config.txt', 'dtparam=spi=', "dtparam=spi=on")
	print "    SPI enabled."
	time.sleep(1)

	print ""

	time.sleep(3)

	print "\n\nSet up screen:"
	time.sleep(2)
	input_incorrect = True
	while input_incorrect:
		rotation = raw_input("    Input the rotation of the screen (0, 90, 180, 270, 360 or leave empty for default setting 270): ")
		if rotation == "":
			input_incorrect = False
			rotation = 270
		elif rotation in ['0', '90', '180', '270']:
			input_incorrect = False
			rotation = int(rotation)
		else:
			print "    Input Error, rotation value must be 0, 90, 180 or 270. Try again or Ctrl + C to Exit."

	line = 'dtoverlay=pitft28-resistive, rotate=%d, speed=48000000, fps=30' % rotation
	edit_line_file('/boot/config.txt', 'dtoverlay=pitft28-resistive', line)
	time.sleep(1)

	edit_cmdline()

	time.sleep(3)

	# 3
	print "\n\nAdd devide"
	time.sleep(2)
	os.system("mv /usr/share/X11/xorg.conf.d/99-fbturbo.conf /home/pi")
	edit_line_file("/home/pi/.profile", "export FRAMEBUFFER=", "export FRAMEBUFFER=/dev/fb1")

	os.system("touch /usr/share/X11/xorg.conf.d/99-pitft.conf")
	file = open("/usr/share/X11/xorg.conf.d/99-pitft.conf", "w")
	device = 'Section "Device"\n    Identifier "PiTFT"\n    Driver "fbdev"\n    Option "fbdev" "/dev/fb1"\nEndSection'
	file.write(device)
	file.close()

	time.sleep(3)
	# 4
	print "\n\nSet auto start X GUI"
	time.sleep(2)
	edit_line_file("/boot/config.txt", "start_x=", "start_x=1")


	print "===================="
	print ""
	print "      Finished!"
	print ""
	print "===================="
	time.sleep(1)
	print "\nReboot.."
	time.sleep(2)
	os.system("sudo reboot")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()