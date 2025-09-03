#include <stdio.h>

int main ()
{
    int num=1 ; 
    for ( num = 1; num < 101; num++)
    {   

        if (num % 3 == 0 && num % 5 == 0)
        {
            printf("FizzBuzz");
            printf(" ");
        }
        else if (num % 3 == 0 )
        {
            printf("Fizz");
            printf(" ");
        }
        else if (num == 100)
        {
            printf("Buzz");    
        }
        else if (num % 5  == 0)
        {
            printf("Buzz");
            printf(" ");
        }
        else
        {
            printf("%d", num);
            printf(" ");
        }  
     }
      printf("\n");
    return(0) ;
}
print("{}".format(chr(number)), end="")