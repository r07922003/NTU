#include "hmm.h"
#include <stdio.h>
#include <stdlib.h>
#define T 2500
#define Test_model_index_num 5

HMM hmm_model[5];
int observation[T][50]; 		//宣告testing_data_arry 
double delta[50][6];			//宣告delta array 
double P[Test_model_index_num];	//宣告 probabilty array 
//int answer[T];				//宣告Testing1 answer array 
void Viterbi_algo(int round,int index)
{
	//-Initailization
	for(int i=0;i<6;i++){
		delta[0][i] = hmm_model[index].initial[i] * hmm_model[index].observation[ observation[round][0] ][i];
	}
	//-Recursion
	double max=0.0;
	for(int t=1;t<50;t++){
		for(int j=0;j<6;j++){
			max=0.0;
			for(int i=0;i<6;i++){
				if(max < (delta[t-1][i] * hmm_model[index].transition[i][j]) ){
					max = (delta[t-1][i] * hmm_model[index].transition[i][j]);
				}
			}
			delta[t][j] = (max * hmm_model[index].observation[ observation[round][t-1] ][j]);
		}
	}
	//-Termination
	max=0.0;
	for(int i=0;i<6;i++){
		if(max < delta[49][i]){
			max = delta[49][i];
		}
	}
	P[index] = max;
}

int select_max_probabilty()
{
	double max=0.0;
	int index=0;
	for(int i=0;i<5;i++){
		if(max < P[i]){
			max = P[i];
			index = i;
		}
	}
	return index;
}

void loadSeqModel(char *seq_model)	//load seqModel A-0,B-1,c-2,D-3,E-4,F-5
{
	FILE *fp = open_or_die(seq_model, "r" );
	char ch;
	int i=0,j=0;
	while((ch=getc(fp))!=EOF){
		if(j<50){
			observation[i][j] = ch-'A';
			j++;
		}
		else{
			j=0;
			i++;
			observation[i][j] = ch-'A';
		}
    }
 //print(observation)
 /*   for(i=0;i<T;i++){
    	for(j=0;j<50;j++){
    		printf("%d",observation[i][j]);
		}
		printf("\n");
	}
*/	
    fclose(fp);
}
/*
void loadTestingAnswer(){
	FILE *fp = open_or_die("testing_answer.txt","r");
	char ch;
	int i=0;
	while((ch=getc(fp))!=EOF){
		switch(ch){
			case '1':
				answer[i] = 0;
				i++;
				break;
			case '2':
				answer[i] = 1;
				i++;
				break;
			case '3':
				answer[i] = 2;
				i++;
				break;
			case '4':
				answer[i] = 3;
				i++;
				break;
			case '5':
				answer[i] = 4;
				i++;
				break;
		}
	}
}
*/
int main(int argc,char *argv[])
{
	// ex: ./test modellist.txt testing_data1.txt result1.txt
	char *modellist = argv[1];	//modellist.txt		parameter save
	char *test_model = argv[2];	//testing_dataX.txt	parameter save
	char *result = argv[3];		//resultX.txt		parameter save
	int select = 0;				//save select modellist
	//double Acc = 0.0;
	/***load modellist and load testing data**********************************************************************/
	load_models(modellist, hmm_model, 5);
	loadSeqModel(test_model);
	//loadTestingAnswer();
	/***out_put result.txt****************************************************************************************/
	FILE *output_model = fopen(result,"w");
	//FILE *output_Acc = fopen("acc.txt","w");
	/*************************************************************************************************************/
	for(int r=0;r<T;r++){
		for(int i=0;i<Test_model_index_num;i++){
			Viterbi_algo(r,i);
		}
		select = select_max_probabilty();
		switch(select)
		{
			case 0:
				fprintf(output_model,"model_01.txt\t%e\n",P[select]);
				break;
			case 1:
				fprintf(output_model,"model_02.txt\t%e\n",P[select]);
				break;
			case 2:
				fprintf(output_model,"model_03.txt\t%e\n",P[select]);
				break;
			case 3:
				fprintf(output_model,"model_04.txt\t%e\n",P[select]);
				break;
			case 4:
				fprintf(output_model,"model_05.txt\t%e\n",P[select]);
				break;
		}
		/*if(answer[r] == select){
			Acc += 1.0;
		}
		*/ 
	}
	//fprintf(output_Acc,"%f",Acc/ (double)T );
	fclose(output_model);
	
	/**Accuracy******************************************************************************************************/
	
	return 0;
}
