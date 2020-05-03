#include<stdio.h>
#include<string.h>
#include<math.h>
#define x 10

void json_data(char* data, int house_id, int sensor_id, float temp, float pressure, float humidity){

    sprintf(data,  
    "{\"meta\":{\"house_id\":%03d,\"sensor_id\":%03d},\"measurements\":{\"pressure(Pa)\":%.2f,\"temperature(C)\":%.2f,\"humidity(perc)\":%.2f}}",
    house_id, sensor_id, pressure, temp, humidity);
    
}

int get_int_len (int value){
  int l=1;
  while(value>9){ l++; value/=10; }
  return l;
}

int main(){


    int my_int = (int) 2.2 + 1222.1 + 1.2;
    int num_digits = get_int_len(my_int);

    for(int i = 0; i < 2; i ++ ){
    char data [113 + num_digits];
    json_data(data, i, 333, 2.2, 2222.2, 2.2);

    printf("%s\n", data);
    }

    printf("%d \n", x);
    

}