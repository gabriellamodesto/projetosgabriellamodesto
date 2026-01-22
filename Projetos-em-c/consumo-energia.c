#include <stdio.h>

void lerConsumos(float *adm, float *prod, float *dep){ // Procedimento para leitura de consumo --> se tornou necessário usar o * para o ponteio
    // Ele guarda um endereço de memória, não um número float
    printf("Digite o consumo do Administrativo: "); // Pergunta
    scanf("%f", adm); // Armazenamento da informação
    printf("Digite o consumo da Produção: ");
    scanf("%f", prod); 
    printf("Digite o consumo do Depósito: ");
    scanf("%f", dep);
}

float mediaConsumo(float a, float b, float c){ // Função para calculo de média
    float media = (a + b + c) / 3;
    return media; // Retorno do valor
}

int setorMaiorConsumo(float a, float b, float c){ // Função para identificar o setor com maior consumo
    int setor = 1; // 1 = Adm 2 = Prod 3 = Dep
    float maior = a; // Enquanto o maior for a, o setor é 1

    if (b > maior){
        maior = b; // Quando maior for b, o setor é 2
        setor = 2;
    }

    if (c > maior)
    {
        maior = c; // Quando maior for c, o setor é 3
        setor = 3;
    }
    
    return setor;
}

void mostrarRelatorio(float adm, float prod, float dep, float media, int maior){ // Procedimento para realizar a impressão dos resultados
    printf("\nConsumo do Administrativo: %.2f kWh\n", adm);
    printf("Consumo da Produção: %.2f kWh\n", prod);
    printf("Consumo do Depósito: %.2f kWh\n", dep);
    printf("\nMédia diária de consumo: %.2f\n", media);
    
    switch (maior) // imprimirá o resultado de maior consumo
    {
    case 1:
        printf("\nSetor que mais consumiu: Administrativo\n");
        break;
    
    case 2:
        printf("\nSetor que mais consumiu: Produção\n");
        break;
    
    case 3:
        printf("\nSetor que mais consumiu: Depósito\n");
        break;
    
    default:
        printf("Consumo balanceado!\n");
        break;
    }
    
}

int gerarAlerta(float valor){
    if (valor > 50){
        return 1; // Acima do limite
    } else {
        return 0; // Dentro do limite
    }
}


int main(){

    float adm, prod, dep;
    float media;
    int maior;

    lerConsumos(&adm, &prod, &dep); // passando o endereço das variaveis, que serão recebidas pelos ponteiros do procedimento
    media = mediaConsumo(adm, prod, dep);
    maior = setorMaiorConsumo(adm, prod, dep);

    mostrarRelatorio(adm, prod, dep, media, maior);

    if (gerarAlerta(adm)){
        printf("\nALERTA: Consumo muito alto no setor Administrativo!\n");
    }

    if (gerarAlerta(prod)){
        printf("\nALERTA: Consumo muito alto no setor de Produção!\n");
    }

    if (gerarAlerta(dep)){
        printf("\nALERTA: Consumo muito alto no setor de Depósito!\n");
    }

    return 0;
}