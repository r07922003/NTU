#include "hmm.h"
//#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#	define T 10000

HMM hmm_initial;
int observation[T][50]; //seq_model_arry 
double alpha[50][6]; 		//alpha array 
double beta[50][6];			//beta array
double gama[50][6];		//gama array
double epislon[49][6][6];	//epislon array 
double alpha_result=0.0;	// alpha 程︽场癬ㄓ诀瞯 
double gama_initial[6];	//gama ╃把计秸俱 
double gama_observarion[6][6];	//gama 锣传 observation把计 
double gama_T_sum[6];			//gama T sum
double gama_Tplus1_sum[6];		//gama T-1 sum
double epislon_sum[6][6];		//epislon_sum T-1 sum 
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

void Forward_algo(int round)
{
	//-Initialization  
	for(int i=0; i < hmm_initial.state_num; i++){
		alpha[0][i] = hmm_initial.initial[i] * hmm_initial.observation[ observation[round][0] ][i];
	}
	//-Induction
	for(int t=1;t < 50;t++){
		for(int j=0;j<6;j++){
			double count=0.0;
			for (int i=0;i<6;i++){
				count = count + (alpha[t-1][i] * hmm_initial.transition[i][j]);
			}
			alpha[t][j]=count * hmm_initial.observation[ observation[round][t] ][j];
		}
	}
	//-Termination
	alpha_result=0.0; 
	for(int i=0;i<6;i++){
		alpha_result += alpha[49][i];
	}
//print(alpha)
/*
	for(int i=0;i<50;i++){
		for(int j=0;j<6;j++){
			printf("%f ",alpha[i][j]);
		}
		printf("\n");
	}
*/
}

void Backward_algo(int round)
{
	//-Initialization
	for(int i=0;i<6;i++){
		beta[49][i]=1.0;
	}
	//-Induction
	for(int t=48;t>=0;t--){
		for(int i=0;i<6;i++){
			beta[t][i]=0.0;
			for(int j=0;j<6;j++){
				beta[t][i] += (hmm_initial.transition[i][j] * hmm_initial.observation[ observation[round][t+1] ][j] * beta[t+1][j]);
			}
		}
	}
	//print(beta)
/*
	for(int i=0;i<50;i++){
		for(int j=0;j<6;j++){
			printf("%f ",beta[i][j]);
		}
		printf("\n");
	}
*/
}

void gama_function()
{
	for(int t=0;t<50;t++){
		for(int i=0;i<6;i++){
			gama[t][i] = (alpha[t][i] * beta[t][i] /  alpha_result); 
		}
	}
}

void Epislon(int round)
{
	for(int t=0;t<49;t++){
		for(int i=0;i<6;i++){
			for(int j=0;j<6;j++){
				epislon[t][i][j] =(alpha[t][i] * hmm_initial.transition[i][j] * hmm_initial.observation[ observation[round][t+1] ][j] * beta[t+1][j] /  alpha_result);
			}
		}
	}
}

void Accumulate(int round)
{
	for(int i=0;i<6;i++){
		/*-----------------------gama Accumulate -----------------------*/
		gama_initial[i] += gama[0][i];
		for(int t=0;t<50;t++){
			if(t != 49){
				gama_Tplus1_sum[i] = gama_Tplus1_sum[i] + gama[t][i];
			}
			gama_T_sum[i] += gama[t][i];
			gama_observarion[observation[round][t]][i] += gama[t][i];
		}
		/*-----------------------Epislon Accumulate -----------------------*/
		for(int j=0;j<6;j++){
			for (int t=0; t < 49; t++){
				epislon_sum[i][j] += epislon[t][i][j];
			}
		}
	}
}

void initial()
{
	for(int i=0;i<6;i++){
		gama_initial[i]=0.0;
		gama_T_sum[i]=0.0;
		gama_Tplus1_sum[i]=0.0;
		for(int j=0;j<6;j++){
			gama_observarion[i][j]=0.0;
			epislon_sum[i][j]=0.0;
		}
	}
}

void Re_estimate()
{
	for (int i=0;i<6;i++){
        hmm_initial.initial[i] = gama_initial[i] / (double)T;
        for (int j=0;j<6;j++){
            hmm_initial.transition[i][j] = epislon_sum[i][j] / gama_Tplus1_sum[i];
            hmm_initial.observation[j][i] = gama_observarion[j][i] / gama_T_sum[i];
        }
    }
}

int main(int argc,char *argv[])
{
	// ex: ./train 100 model_init.txt seq_model_01.txt model_01.txt   
	int iter = atoi(argv[1]);	//iteration			parameter save
	char *model_init = argv[2];	//model_init.txt	parameter save
	char *seq_model = argv[3];	//seq_model_0X.txt	parameter save
	char *output =argv[4];		//model_0X.txt		parameter save
	/*Load Data************************************************************************************************************************/ 
	loadHMM( &hmm_initial,model_init);
	loadSeqModel(seq_model);
	/*Start Train**********************************************************************************************************************/
	for(int i=0;i<iter;i++){
		initial();
		printf("iter=%d\n",i);
		for(int t=0;t<T;t++){
			Forward_algo(t);
			Backward_algo(t);
			gama_function();
			Epislon(t);
			Accumulate(t);
		}
		Re_estimate();
	}
	/************************************************************************************************************************************/
	FILE *output_model = fopen(output,"w");
	dumpHMM(output_model, &hmm_initial );
	fclose(output_model);
	return 0;
}
