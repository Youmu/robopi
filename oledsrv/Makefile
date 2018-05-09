out/oled:out/oled.o out/ssd1331.o
	gcc -Wall -o out/oled out/oled.o out/ssd1331.o -lbcm2835
out/ssd1331.o:ssd1331.c ssd1331.h out
	gcc -Wall -c ssd1331.c -o out/ssd1331.o -lbcm2835
out/oled.o:oled.c ssd1331.h out
	gcc -Wall -c oled.c -o out/oled.o -lbcm2835
out:
	mkdir out
clean:
	rm -r out
