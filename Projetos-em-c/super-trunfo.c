#include <stdio.h>

//funções

float cal_pib_densidade(float n1, float n2) 
{ return n1 / n2;
}

float calcular_super_poder (int populacao, float area, float pib, int pontos, float pib_percapita, float densidade)
{ return populacao + area + pib + pontos + pib_percapita + (1 / densidade);
}

int main() {

    //Declaração de variáveis da primeira carta

    char estado1, codigo1[4], cidade1[30];
    int pontosturisticos1;
    unsigned long int populacao1;
    float area1, pib1, densidade_populacional1, pib_percapita1, super1;

    //Entrada da primeira carta

    printf("Escolha uma estado (A a H): ");
    scanf(" %c", &estado1);

    printf("Digite o código da carta (exemplo: A01 ou F04): ");
    scanf("%s", codigo1);

    printf("Informe uma cidade: ");
    scanf(" %[^\n]", cidade1); // Para informar nome cidade composto

    printf("Indique o número de habitantes da cidade escolhida: ");
    scanf("%lu", &populacao1);

    printf("Informe a área da cidade: ");
    scanf("%f", &area1);

    printf("Indique o PIB da cidade: ");
    scanf("%f", &pib1);

    printf("Indique o número de pontos turísticos: ");
    scanf("%d", &pontosturisticos1);

    densidade_populacional1 = (float) cal_pib_densidade(populacao1, area1); //chamada da função

    pib_percapita1 = (float) cal_pib_densidade(pib1 * 1000000000, populacao1); //chamada da função

    super1 = (float) calcular_super_poder(populacao1, area1, pib1, pontosturisticos1, pib_percapita1, densidade_populacional1); //chamada da função

    //Declaração de variáveis da segunda carta

    char estado2, codigo2 [4], cidade2 [30];
    int pontosturisticos2;
    unsigned long int populacao2;
    float area2, pib2, densidade_populacional2, pib_percapita2, super2;

    //Entrada da segunda carta

    printf("Escolha uma estado (A a H): ");
    scanf(" %c", &estado2);

    printf("Digite o código da carta (exemplo: A01 ou F04): ");
    scanf("%s", codigo2);

    printf("Informe uma cidade do estado escolhido: ");
    scanf(" %[^\n]", cidade2); // Para informar nome de cidade composto

    printf("Indique o número de habitantes da cidade escolhida: ");
    scanf("%lu", &populacao2);

    printf("Informe a área da cidade: ");
    scanf("%f", &area2);

    printf("Indique o PIB da cidade: ");
    scanf("%f", &pib2);

    printf("Indique o número de pontos turísticos: ");
    scanf("%d", &pontosturisticos2);

    densidade_populacional2 = (float) cal_pib_densidade(populacao2, area2); //chamada da função

    pib_percapita2 = (float) cal_pib_densidade(pib2 * 1000000000, populacao2); //chamada da função

    super2 = (float) calcular_super_poder(populacao2, area2, pib2, pontosturisticos2, pib_percapita2, densidade_populacional2);


    //Saída da primeira carta

    printf("Código da Carta: %s\n", codigo1);
    printf("Estado: %c\n", estado1);
    printf("Cidade: %s\n", cidade1);
    printf("População: %lu\n", populacao1);
    printf("Área: %.2f km²\n", area1);
    printf("PIB: R$ %.2f bilhões\n", pib1);
    printf("Pontos turísticos: %d\n", pontosturisticos1);
    printf("A densidade populacional da cidade é: %.2f habitantes por km²\n", densidade_populacional1);
    printf("O PIB per capita da cidade é: R$ %.2f \n", pib_percapita1);


    //Saída da segunda carta

    printf("Código da Carta: %s\n", codigo2);
    printf("Estado: %c\n", estado2);
    printf("Cidade: %s\n", cidade2);
    printf("População: %lu\n", populacao2);
    printf("Área: %.2f km²\n", area2);
    printf("PIB: R$ %.2f bilhões\n", pib2);
    printf("Pontos turísticos: %d\n", pontosturisticos2);
    printf("A densidade populacional da cidade é: %.2f habitantes por km² \n", densidade_populacional2);
    printf("O PIB per capita da cidade é: R$ %.2f \n", pib_percapita2);

    int opcao;

    printf("***Escolha o atributo para se comparar***\n");
    printf("1. População\n");
    printf("2. Área\n");
    printf("3. PIB\n");
    printf("4. Número de pontos turísticos\n");
    printf("5. Densidade populacional\n");
    printf("Escolha a sua opção: ");
    scanf("%d", &opcao);

    // Comparação

    printf("\n---- Resultado da Comparação ----\n");
    printf("Carta 1 - Cidade: %s\n", cidade1);
    printf("Carta 2 - Cidade: %s\n", cidade2);

    // Resultados do jogo

    switch (opcao)
    {
    case 1:
        if (populacao1 > populacao2) {
            printf("População: Carta 1 vence (1)\n");
        } else if (populacao1 < populacao2) {
            printf("População: Carta 2 vence (0)\n");
        } else {
            printf("Empate!\n");
        }
        break;
    
    case 2:
        if (area1 > area2) {
            printf("Área: Carta 1 vence (1)\n");
        } else if (area1 < area2) {
            printf("Área: Carta 2 vence (0)\n");
        } else {
            printf("Empate!\n");
        }
        break;

    case 3:
        if (pib1 > pib2) {
            printf("PIB: Carta 1 vence (1)\n");
        } else if (pib1 < pib2) {
            printf("PIB: Carta 2 vence (0)\n");
        } else {
            printf("Empate!\n");
        }
        break;

    case 4:
        if (pontosturisticos1 > pontosturisticos2) {
            printf("Pontos Turísticos: Carta 1 vence (1)\n");
        } else if (pontosturisticos1 < pontosturisticos2) {
            printf("Pontos Turísticos: Carta 2 vence (0)\n");
        } else {
            printf("Empate!\n");
        }
        break;
        
    case 5:
        if (densidade_populacional1 < densidade_populacional2) {
            printf("Densidade Populacional (menor vence): Carta 1 vence (1)\n");
        } else if (densidade_populacional1 > densidade_populacional2) {
            printf("Densidade Populacional (menor vence): Carta 2 vence (0)\n");
        } else {
            printf("Empate!\n");
        }
        break;

    default:
        printf("Opção inválida!\n");
    break;

    }
    
    return 0;

}