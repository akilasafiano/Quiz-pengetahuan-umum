#include<stdio.h>
#include<conio.h>
#include <windows.h>
#include<ctype.h>
#include<stdlib.h>
#include<time.h>
#include<dos.h>

void displayscore()
 {
 char name[20];
 float s;
 FILE *f;
 system("cls");
 f=fopen("score.txt","r");
 fscanf(f,"%s%f",&name,&s);
 printf("\n\n\t\t ");
 printf("\n\n\t\t %s has secured the Highest Score %.2f",name,s);
 printf("\n\n\t\t ");
 fclose(f);
 getch();
 }



void help()
 {
 system("cls");
 printf("\n\n\n\tThis game is very easy to play. You'll be asked some general");
 printf("\n\n\tknowledge questions and the right answer is to be chosen among");
 printf("\n\n\tthe four options provided. Your score will be calculated at the");
 printf("\n\n\tend. Remember that the more quicker you give answer the more");
 printf("\n\n\tscore you will secure. Your score will be calculated and displayed");
 printf("\n\n\tat the end and displayed. If you secure highest score, your score");
 printf("\n\n\twill be recorded. So BEST OF LUCK.");
 }
void writescore(float score, char plnm[20])
 {
 float sc;
 char nm[20];
 FILE *f;
 system("cls");
 f=fopen("score.txt","r");
 fscanf(f,"%s%f",&nm,&sc);
 if (score>=sc)
   { sc=score;
     fclose(f);
     f=fopen("score.txt","w");
     fprintf(f,"%s\n%.2f",plnm,sc);
     fclose(f);
   }
 }
int main()
     {
     int countq,countr;
     int r,i;
     int pa;int nq[6];int w;
     float score;
     char choice;
     char playername[20];
     time_t initialtime,finaltime;
     system("cls");
     //randomize();
     mainhome:
     system("cls");
     puts("\n\t\t WELCOME TO I.Q. TEST PROGRAM\n\n") ;
     puts("\n\t\t-------------------------------");
     puts("\n\t\t Enter 'S' to start game       ");
     puts("\n\t\t Enter 'V' to view high score  ");
     puts("\n\t\t Enter 'H' for help            ");
     puts("\n\t\t Enter 'Q' to quit             ");
     printf("\n\t\t-------------------------------\n\n\t\t  ");
     choice=toupper(getch());
     if (choice=='V')
 {
 displayscore();
 goto mainhome;
 }
     else if (choice=='Q')
 exit(1);
     else if (choice=='H')
 {
 help();
 getch();
 goto mainhome;
 }
    else if(choice=='S'){
     system("cls");

     printf("\n\n\n\t\t\tEnter your name...");
     printf("\n\t\t\t(only one word)\n\n\t\t\t");
     gets(playername);

     home:
     system("cls");
     initialtime=time(NULL);
     countq=countr=0;
     i=1;
     start:
     srand ( time(NULL) );
     r=rand()%15+1;
     nq[i]=r;
     for (w=0;w<i;w++)
 if (nq[w]==r) goto start;

     switch(r)
  {
  case 1:
  printf("\n\nApa nama Universitas swasta tertua di Indonesia?");
  printf("\n\nA.UII\tB.UMM\n\nC.UNHAN\tD.UPN\n\n");
  countq++;
  if (toupper(getch())=='A')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is A.4");break;}

  case 2:
  printf("\n\n\nHewan apa yang paling cepat di darat?");
  printf("\n\nA.Cheetah\tB.Serigala\n\nC.Puma\tD.Harimau\n\n");
  countq++;
  if (toupper(getch())=='A')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is A.Cheetah");break;}

  case 3:
  printf("\n\n\nSiapa Presiden pertama Amerika Serikat?");
  printf("\n\nA.Richard Nikson\tB.Abraham Linkon\n\nC.John F. Kennedy\tD.George Washington\n\n");
  countq++;
  if (toupper(getch())=='D')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is D.George Washington");break;}


  case 4:
  printf("\n\n\nSiapa penemu bola lampu listrik pertama di dunia?");
  printf("\n\nA.Thomas Alva Edison\tB.Nikola Tesla\n\nC.Alexander Graham Bell\tD.Benjamin Franklin\n\n");
  countq++;
  if (toupper(getch())=='A')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is A.Thomas Alva Edison");break;}


  case 5:
  printf("\n\n\nDi tahun berapa Perang Dunia II berakhir?");
  printf("\n\nA.1945\tB.1939\n\nC.1941\tD.1950\n\n");
  countq++;
  if (toupper(getch())=='A')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is A.1945");break;}

  case 6:
  printf("\n\n\nBahasa pemograman mana yang paling sering digunakan dalam pengembangan website?");
  printf("\n\nA.Phython\tB.HTML\n\nC.Java\tD.PHP\n\n");
  countq++;
  if (toupper(getch())=='B' )
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is B.HTML");break;}


  case 7:
  printf("\n\n\nBahasa resmi apa yang digunakan di Brasil");
  printf("\n\nA.Inggris\tB.Prancis\n\nC.Portugis\tD.Spanyol\n\n");
  countq++;
  if (toupper(getch())=='C')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is C.Portugis");break;}


  case 8:
  printf("\n\n\nBerapa ketinggian Gunung Everest diatas kaki?");
  printf("\n\nA.8648\tB.6648\n\nC.8884\tD.8848\n\n");
  countq++;
  if (toupper(getch())=='D')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is D.8848");break;}


  case 9:
  printf("\n\n\nApa singkatan dari PDB dalam ekonomi?");
  printf("\n\nA.Produk Domestik Bruto\tB.Produk Daya Beli\n\nC.Produk Dunia Baku\t\tD.Pendapatan Dasar Bersih\n\n");
  countq++;
  if (toupper(getch())=='A')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is A.Produk Domestik Bruto");break;}


  case 10:
  printf("\n\n\nSistem pemerintahan di Indonesia menganut prinsip apa?");
  printf("\n\nA.Republik Parlementer\tB.Monarki Konstitusional\n\nC.Republik Presidensial\tD.Dempokrasi Sosialis\n\n");
  countq++;
  if (toupper(getch())=='C')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is C.Republik Presidensial");break;}


  case 11:
  printf("\n\n\nSiapa yang mengungkapkan slogan "Cogito, ergo sum" yang berarti "Saya berfikir, maka saya ada"?");
  printf("\n\nA.Friedrich Nietzsche\tB.Immanuel Kant\n\nC.Rene` Descartes\tD.John Locke\n\n");
  countq++;
  if (toupper(getch())=='C')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is C.Rene` Descartes");break;}

  case 12:
  printf("\n\n\nAlat apa yang digunakan untuk mengukur gaya?");
  printf("\n\nA.Amperemeter\tB.Dinamometer\n\nC.Barometer\tD.Termometer\n\n");
  countq++;
  if (toupper(getch())=='B')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is B.Dinamometer");break;}

  case 13:
  printf("\n\n\nApa nama planet terdekat dengan matahari?");
  printf("\n\nA.Merkurius\tB.Venus\n\nC.Bumi\tD.Mars\n\n");
  countq++;
  if (toupper(getch())=='A')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is A.South Africa");break;}

  case 14:
  printf("\n\n\nApa yang dimaksud dengan 'cloud computing'?");
  printf("\n\nA.Penyimpanan data di perangkat lokal\tB.Pengolahan data menguunakan server jarak jauh melalui intenet\n\nC.Sistem operasi berbasis web\tD.Jaringan komputer tanpa kabel\n\n");
  countq++;
  if (toupper(getch())=='B')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is B.Pengolahan data menguunakan server jarak jauh melalui intenet");break;}

  case 15:
  printf("\n\n\nSiapa penulis novel 'Bumi Manusia'?");
  printf("\n\nA.Andrea Hirata\tB.Pramoedya Ananta Toer\n\nC.Tere Liye\tD.Habiburrahman El Shirazy\n\n");
  countq++;
  if (toupper(getch())=='B')
   {printf("\n\nCorrect!!!");countr++; break;}
  else
         {printf("\n\nWrong!!! The correct answer is B.Pramoedya Ananta Toer");break;}

  }
 i++;
 if (i<=5) goto start;
 finaltime=time(NULL);
 score=(float)countr/countq*100-difftime(finaltime,initialtime)/3;
 if (score<0) score=0;
 printf("\n\n\nYour Score: %.2f",score);
 if (score==100) printf("\n\nEXCELLENT!!! KEEP IT UP");
 else if (score>=80 && score<100) printf("\n\nVERY GOOD!!");
 else if (score>=60 &&score<80) printf("\n\nGOOD! BUT YOU NEED TO KNOW MORE.");
 else if (score>=40 && score<60) printf("\n\nSATISFACTORY RESULT, BUT THIS MUCH IS MUCH SUFFICIENT.");
 else printf("\n\nYOU ARE VERY POOR IN G.K.,WORK HARD");
 puts("\n\nNEXT PLAY?(Y/N)");
 if (toupper(getch())=='Y')
  goto home;
 else
  {
  writescore(score,playername);
  goto mainhome;
  }
 }
     else
 {
 printf("\n\n\t\t  Enter the right key\n\n\t\t  ");
 Sleep(700);
 goto mainhome;
 }
 return 0;
}
