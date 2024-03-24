#include<vector> 
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <math.h>  
#include <algorithm>
#include "Variable.hpp"


struct Regression{

    float coefficient;
    float intercept;
    float covariance;
    float R_square;
    float x_mean;  
    float y_mean; 

    std::vector<Variable>* observation; 

    Regression(){
        coefficient = 0; 
        intercept = 0;
        covariance = 0;
        float r_square = 0;
        float x_mean = 0;
        observation = new std::vector<Variable>; 

        std::cout << "Regression is initialized" << std::endl;





    }
    
    void readData(std::string name){
        std::ifstream file(name);

        if(file){
            
        }




    }




};