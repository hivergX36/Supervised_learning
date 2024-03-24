#include<vector> 
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <math.h>  
#include <algorithm>

struct Variable{

    std::vector<float> * y_label;
    std::vector<float> * x_predictor; 

    Variable(){
        y_label = new std::vector<float>;
        x_predictor = new std::vector<float>; 
  



        
    }




};