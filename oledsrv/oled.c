/*****************************************************************************
*
* File                : oled.c
* Hardware Environment: Raspberry Pi
* Build Environment   : GCC
* Version             : V1.0.7
* Author              : Yehui
*
*              (c) Copyright 2005-2017, WaveShare
*                   http://www.waveshare.com
*                   http://www.waveshare.net   
*                      All Rights Reserved
*              
******************************************************************************/

#include <bcm2835.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include "ssd1331.h"
#include <ifaddrs.h>
#include <netinet/in.h> 
#include <string.h> 
#include <arpa/inet.h>
#include <net/if.h>

char value[10] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
int main(int argc, char **argv)
{
    char msg[20];
    struct ifaddrs * ifAddrStruct=NULL;
    struct ifaddrs * ifa=NULL;
    void * tmpAddrPtr=NULL;

    time_t now;
    struct tm *timenow;
    FILE *pFile = fopen("icon.bmp", "r");
    /* 1 pixel of 888 bitmap = 3 bytes */
    size_t pixelSize = 3;
    unsigned char bmpBuffer[OLED_WIDTH * OLED_HEIGHT * 3];

    if(!bcm2835_init())
    {
        return -1;
    }
    if (pFile == NULL) {
        printf("file not exist\n");
        return 0;
    }
    fseek(pFile, 54, 0);
    fread(bmpBuffer, pixelSize, OLED_WIDTH * OLED_HEIGHT, pFile);
    fclose(pFile);

    printf("OLED example. Press Ctrl + C to exit.\n");
    SSD1331_begin();
    SSD1331_bitmap24(0, 0, bmpBuffer, 96, 64);
    SSD1331_display();
    bcm2835_delay(2000);

    SSD1331_clear();
    while(1)
    {
	usleep(500000);
	int h = 16;
        time(&now);
        timenow = localtime(&now);
        sprintf(msg, "%2d:%2d:%2d", timenow->tm_hour, timenow->tm_min, timenow->tm_sec);
	SSD1331_string(0, 0, msg, 12, 1, WHITE);
        getifaddrs(&ifAddrStruct);
	for (ifa = ifAddrStruct; ifa != NULL; ifa = ifa->ifa_next) {
	    if(!ifa->ifa_addr || (ifa->ifa_flags & IFF_LOOPBACK)){
	        continue;
	    }
	    if(ifa->ifa_addr->sa_family == AF_INET){
	        tmpAddrPtr=&((struct sockaddr_in *)ifa->ifa_addr)->sin_addr;
		char addressBuffer[INET_ADDRSTRLEN];
		inet_ntop(AF_INET, tmpAddrPtr, addressBuffer, INET_ADDRSTRLEN);
		sprintf(msg, "%s", ifa->ifa_name); 
	        SSD1331_string(0,h,msg, 12,1,WHITE);
		sprintf(msg, " %s", addressBuffer); 
	        SSD1331_string(0,h+11,msg, 12,1,WHITE);
		h += 24;
	    }
	}
        if (ifAddrStruct!=NULL) freeifaddrs(ifAddrStruct); 
        SSD1331_display();
    }
    bcm2835_spi_end();
    bcm2835_close();
    return 0;
}

