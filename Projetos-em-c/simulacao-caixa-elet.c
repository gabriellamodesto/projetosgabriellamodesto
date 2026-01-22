#include <stdio.h>

int main(){

    int valor_saque;
    int nota_cem = 0, nota_cinquenta = 0, nota_vinte = 0, nota_dez = 0; // A quantidade de notas precisa começar em 0

    printf("Digite o valor do saque: ");
    scanf("%d", &valor_saque);

    if (valor_saque %10 != 0){
        printf("Erro: apenas múltiplos de 10\n");
    } else {

        if (valor_saque >= 100){
            nota_cem = valor_saque / 100;
            valor_saque = valor_saque % 100;
        } if (valor_saque >= 50){
            nota_cinquenta = valor_saque / 50;
            valor_saque = valor_saque % 50;
        } if (valor_saque >= 20){
            nota_vinte = valor_saque / 20;
            valor_saque = valor_saque % 20;
        } if (valor_saque >= 10){
            nota_dez = valor_saque / 10;
            valor_saque = valor_saque % 10;
        }
    }

    if (nota_cem > 0){
        printf("%d de nota(s) de 100\n", nota_cem);
    }
    if (nota_cinquenta > 0){
        printf("%d de nota(s) de 50\n", nota_cinquenta);
    }
      if (nota_vinte > 0){
        printf("%d de nota(s) de 20\n", nota_vinte);
    }
      if (nota_dez > 0){
        printf("%d de nota(s) de 10\n", nota_dez);
    }

   return 0;
}