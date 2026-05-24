#include <stdio.h>
#include <windows.h>
#include <stdlib.h>

void draw_table(char board[]) {
    printf(" %c | %c | %c \n", board[0], board[1], board[2]);
    printf("---+---+---\n");
    printf(" %c | %c | %c \n", board[3], board[4], board[5]);
    printf("---+---+---\n");
    printf(" %c | %c | %c \n", board[6], board[7], board[8]);
    
}

int check_win(char board[]) {  
if (board[0] == board[1] && board[1] == board[2]) return 1;
if (board[3] == board[4] && board[4] == board[5]) return 1;
if (board[6] == board[7] && board[7] == board[8]) return 1;
if (board[0] == board[3] && board[3] == board[6]) return 1;
if (board[1] == board[4] && board[4] == board[7]) return 1;
if (board[2] == board[5] && board[5] == board[8]) return 1;
if (board[0] == board[4] && board[4] == board[8]) return 1;
if (board[2] == board[4] && board[4] == board[6]) return 1;

    return 0;
}

int main(void) {
    SetConsoleCP(65001);
    SetConsoleOutputCP(65001);
    char boar[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
    char name1[50];
    char name2[50];
    int hod=0,choice,flag=0;
    printf("Игра крестики-нолики\n");
    printf("Введите имя 1 игрока(X): ");
    scanf("%s",name1);
    printf("Введите имя 2 игрока(O): ");
    scanf("%s",name2);
    draw_table(boar);
    printf("\nИгрок 1 — %s\nИгрок 2 — %s\n", name1, name2);
    while (hod<9){
        if (hod%2==0){
            printf("Ход %s: ",name1);
            scanf("%d",&choice);
            int index=choice-1;
            if(choice>=1 && choice<=9 && boar[index]!='X' && boar[index]!='O'){
                boar[index]='X';
                hod++;
                system("cls");
                draw_table(boar);
                if (check_win(boar)==1){
                    printf("Победил %s!\n",name1);
                    flag+=1;
                    break;
                }
            }else{
                printf("Клетка занята или введена не правильно!\n");
                continue;
            }
        }else{
            printf("Ход %s: ",name2);
            scanf("%d",&choice);
            int ind=choice-1;
            if(choice>=1 && choice<=9 && boar[ind]!='X' && boar[ind]!='O'){
                boar[ind]='O';
                hod++;
                system("cls");
                draw_table(boar);
                if (check_win(boar)==1){
                    printf("Победил %s!\n",name2);
                    flag+=1;
                    break;
                }
            }else{
                printf("Клетка занята или введена не правильно!\n");
                continue;
        }
    }
    }
    if (flag==0){printf("Ничья\n");}
    return 0;
}
