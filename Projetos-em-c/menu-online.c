#include <stdio.h>
#include <locale.h>

int main(){

    int i;
    int opcao = 0;
    int continuar_pedido = 1;
    float valor_hamburguer = 26.00, valor_hamburguer_combo = 38.00, valor_pizza = 60.00;
    float valor_suco = 12.00, valor_agua = 3.00, valor_refrigerante = 6.00;
    float valor_banoffe = 20.00, valor_brownie = 15.00;
    float total = 0.00;

    setlocale(LC_ALL, "pt_BR.UTF-8");

    printf("\t\t------Menu do restaurante da Gabriella------\n");

    //Exibição do menu

    for (i = 1; i <= 9; i++){

        if (i == 1){
            printf("1 - Hamburguer: R$ %.2f\n", valor_hamburguer);
        } else if (i == 2) {
            printf("2 - Combo: Hamburguer + batata + refrigerante: R$ %.2f\n", valor_hamburguer_combo);
        } else if (i == 3){
            printf("3 - Pizza grande: R$ %.2f\n", valor_pizza);
        } else if (i == 4){
            printf("4 - Suco natural: R$ %.2f\n", valor_suco);
        } else if (i == 5){
            printf("5 - Refrigerante: R$ %.2f\n", valor_refrigerante);
        } else if (i == 6){
            printf("6 - Água: R$ %.2f\n", valor_agua);
        } else if (i == 7){
            printf("7 - Banoffe: R$ %.2f\n", valor_banoffe);
        } else if (i == 8){
            printf("8 - Brownie: R$ %.2f\n", valor_brownie);
        } else if (i == 9) {
            printf("9 - Encerrar pedido.\n");
        }
        
        //Loop para escolha de pedido 
    }

        while (continuar_pedido == 1){              // Enquanto a variável "continuar_pedido" for igual a 1, o usuário pode continuar no menu
        printf("Digite o número do item que você deseja: ");
        scanf("%d", &opcao);

            if (opcao == 1){
                total += valor_hamburguer;
                printf("Opção escolhida: Hamburguer\nTotal parcial: R$ %.2f\n", total);
            } else if (opcao == 2){
                total += valor_hamburguer_combo;
                printf("Opção escolhida: Combo: Hamburguer + batata + refrigerante\nTotal parcial: R$ %.2f\n", total);
            } else if (opcao == 3){
                total += valor_pizza;
                printf("Opção escolhida: Pizza grande\nTotal parcial: R$ %.2f\n", total);
            } else if (opcao == 4){
                total += valor_suco;
                printf("Opção escolhida: Suco\nTotal parcial: R$ %.2f\n", total);
            } else if (opcao == 5){
                total += valor_refrigerante;
                printf("Opção escolhida: Refrigerante\nTotal parcial: R$ %.2f\n", total);
            } else if (opcao == 6){
                total += valor_agua;
                printf("Opção escolhida: Água\nTotal parcial: R$ %.2f\n", total);
            } else if (opcao == 7){
                total += valor_banoffe;
                printf("Opção escolhida: Banoffe\nTotal parcial: R$ %.2f\n", total);
            } else if (opcao == 8){
                total += valor_brownie;
                printf("Opção escolhida: Brownie\nTotal parcial: R$ %.2f\n", total);
            } else if (opcao == 9){
                continuar_pedido = 0; // aqui, a opção nove tem o valor de continuar pedido = 0, encerrando o programa.
            } else {
                printf("Opção inválida. Escolha um item disponível no menu!\n");
            }

            if (opcao >= 1 && opcao <= 8){ // aqui, o programa irá entender que se as escolhas forem entre 1 e 8, há itens a serem guardados na memória.
                printf("Deseja pedir mais alguma coisa? (1 para Sim, 0 para Não): ");
                scanf("%d", &continuar_pedido);
                while (continuar_pedido !=1 && continuar_pedido != 0){ // condição while para colocar apenas dois valores válidos no continuar_pedido
                    printf("Opção inválida. Por favor, digite 1 para continuar ou 0 para encerrar: ");
                    scanf("%d", &continuar_pedido); 
                }
            }

        }

        if (total > 0){ // para não aparecer "Total do pedido = 0.00" quando escolhido 9, encerrando o pedido.
            printf("Total do pedido: %.2f\n", total);
        }
        
        if (total >= 80.00){ // brindes
            printf("Parabéns! Você ganhou uma sobremesa gratuita!\n");
        } else if (total >= 60.00){
            printf("Parabéns! Você ganhou um cupom de 10%% de desconto para a próxima compra + um brinde!\n");
        } else if (total >= 40.00){
            printf("Parabéns! Você ganhou um cupom de 10%% de desconto para a próxima compra!\n");
        } else if (total < 40 && total != 0) {
            printf("Infelizmente, o valor mínimo para alguma premiação não foi atingido.\n");
        } else {
            printf("Pedido encerrado! Obrigado!\n");
        }



    return 0;
}