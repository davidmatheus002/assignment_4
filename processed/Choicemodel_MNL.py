# Translated to .py by Marti Montesinos

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_CAR	 = Beta('ASC_CAR',0,-30,30,0)
ASC_SBB	 = Beta('ASC_SBB',0,-10,10,1)
ASC_SM	 = Beta('ASC_SM',0,-30,30,0)
B_COST	 = Beta('B_COST',0,-10,10,0)
B_HE	 = Beta('B_HE',0,-10,10,0)
B_TIME	 = Beta('B_TIME',0,-10,10,0)

for i in range(1, 41):
    globals()['ASC_%s' % i]= Beta(f'ASC_{i}', 0, -30,30, 0')
#ASC_1    = Beta('ASC_1', 0,-30, 30, 0)
#ASC_2    = Beta('ASC_2', 0,-30, 30, 0)
#ASC_3    = Beta('ASC_3', 0,-30, 30, 0)
#ASC_4    = Beta('ASC_4', 0,-30, 30, 0)
#ASC_5    = Beta('ASC_5', 0,-30, 30, 0)
#ASC_6    = Beta('ASC_6', 0,-30, 30, 0)
#ASC_7    = Beta('ASC_7', 0,-30, 30, 0)
#ASC_8    = Beta('ASC_8', 0,-30, 30, 0)
#ASC_9    = Beta('ASC_9', 0,-30, 30, 0)
#ASC_10   = Beta('ASC_10', 0,-30, 30, 0)
#ASC_11   = Beta('ASC_11', 0,-30, 30, 0)
#ASC_12   = Beta('ASC_12', 0,-30, 30, 0)
#ASC_13   = Beta('ASC_13', 0,-30, 30, 0)
#ASC_14   = Beta('ASC_14', 0,-30, 30, 0)
#ASC_15   = Beta('ASC_15', 0,-30, 30, 0)
#ASC_16   = Beta('ASC_16', 0,-30, 30, 0)
#ASC_17   = Beta('ASC_17', 0,-30, 30, 0)
#ASC_18   = Beta('ASC_18', 0,-30, 30, 0)
#ASC_19   = Beta('ASC_19', 0,-30, 30, 0)
#ASC_20   = Beta('ASC_20', 0,-30, 30, 0)
#ASC_21   = Beta('ASC_21', 0,-30, 30, 0)
#ASC_22   = Beta('ASC_22', 0,-30, 30, 0)
#ASC_23   = Beta('ASC_23', 0,-30, 30, 0)
#ASC_24   = Beta('ASC_24', 0,-30, 30, 0)
#ASC_25   = Beta('ASC_25', 0,-30, 30, 0)
#ASC_26   = Beta('ASC_26', 0,-30, 30, 0)
#ASC_27   = Beta('ASC_27', 0,-30, 30, 0)
#ASC_28   = Beta('ASC_28', 0,-30, 30, 0)
#ASC_29   = Beta('ASC_29', 0,-30, 30, 0)
#ASC_30   = Beta('ASC_30', 0,-30, 30, 0)
#ASC_31   = Beta('ASC_31', 0,-30, 30, 0)
#ASC_32   = Beta('ASC_32', 0,-30, 30, 0)
#ASC_33   = Beta('ASC_33', 0,-30, 30, 0)
#ASC_34   = Beta('ASC_34', 0,-30, 30, 0)
#ASC_35   = Beta('ASC_35', 0,-30, 30, 0)
#ASC_36   = Beta('ASC_36', 0,-30, 30, 0)
#ASC_37   = Beta('ASC_37', 0,-30, 30, 0)
#ASC_38   = Beta('ASC_38', 0,-30, 30, 0)
#ASC_39   = Beta('ASC_39', 0,-30, 30, 0)
#ASC_40   = Beta('ASC_40', 0,-30, 30, 1)
B_DIRECT_NEXT= Beta('B_DIRECT_NEXT', 0, -10, 10, 0)
B_PEOPLE_AROUND= Beta('B_PEOPLE_AROUND', 0, -10, 10,0)
B_WINDOWWALL= Beta('B_WINDOWWALL', 0, -10, 10, 0)
B_DISTANCE= Beta('B_DISTANCE', 0, -10, 10, 0)
B_24SEAT= Beta('B_24SEAT', 0, -10, 10, 0)
B_GENDER= Beta('B_GENDER', 0, -10, 10, 0)
B_AGE = Beta('B_AGE', 0, -10, 10, 0)



# Define here arithmetic expressions for name that are not directly 
# available from the data


CAR_AV_SP  = DefineVariable('CAR_AV_SP', CAR_AV    *  (  SP   !=  0  ))
SM_COST  = DefineVariable('SM_COST', SM_CO   * (  GA   ==  0  ))
TRAIN_AV_SP  = DefineVariable('TRAIN_AV_SP', TRAIN_AV    *  (  SP   !=  0  ))
TRAIN_COST  = DefineVariable('TRAIN_COST', TRAIN_CO   * (  GA   ==  0  ))
one  = DefineVariable('one',1)


#SEAT1_AV= DefineVariable('SEAT1_AV', SEAT_1AV)
#SEAT2_AV= DefineVariable('SEAT2_AV', SEAT_2AV)
#SEAT3_AV= DefineVariable('SEAT3_AV', SEAT_3AV)
#SEAT4_AV= DefineVariable('SEAT4_AV', SEAT_4AV)
#SEAT5_AV= DefineVariable('SEAT5_AV', SEAT_5AV)
#SEAT6_AV= DefineVariable('SEAT6_AV', SEAT_6AV)
#SEAT7_AV= DefineVariable('SEAT7_AV', SEAT_7AV)
#SEAT8_AV= DefineVariable('SEAT8_AV', SEAT_8AV)
#SEAT9_AV= DefineVariable('SEAT9_AV', SEAT_9AV)
#SEAT10_AV= DefineVariable('SEAT10_AV', SEAT_10AV)
#SEAT11_AV= DefineVariable('SEAT11_AV', SEAT_11AV)
#SEAT12_AV= DefineVariable('SEAT12_AV', SEAT_12AV)
#SEAT13_AV= DefineVariable('SEAT13_AV', SEAT_13AV)
#SEAT14_AV= DefineVariable('SEAT14_AV', SEAT_14AV)
#SEAT15_AV= DefineVariable('SEAT15_AV', SEAT_15AV)
#SEAT16_AV= DefineVariable('SEAT16_AV', SEAT_16AV)
#SEAT17_AV= DefineVariable('SEAT17_AV', SEAT_17AV)
#SEAT18_AV= DefineVariable('SEAT18_AV', SEAT_18AV)
#SEAT19_AV= DefineVariable('SEAT19_AV', SEAT_19AV)
#SEAT20_AV= DefineVariable('SEAT20_AV', SEAT_20AV)
#SEAT21_AV= DefineVariable('SEAT21_AV', SEAT_21AV)
#SEAT20_AV= DefineVariable('SEAT22_AV', SEAT_22AV)
#SEAT20_AV= DefineVariable('SEAT23_AV', SEAT_23AV)
#SEAT20_AV= DefineVariable('SEAT24_AV', SEAT_24AV)
#SEAT20_AV= DefineVariable('SEAT25_AV', SEAT_25AV)
#SEAT20_AV= DefineVariable('SEAT26_AV', SEAT_26AV)
#SEAT20_AV= DefineVariable('SEAT27_AV', SEAT_27AV)
#SEAT20_AV= DefineVariable('SEAT28_AV', SEAT_28AV)
#SEAT20_AV= DefineVariable('SEAT29_AV', SEAT_29AV)









#Utilities
Car_SP = ASC_CAR  * one + B_TIME * CAR_TT + B_COST * CAR_CO
SBB_SP = ASC_SBB  * one + B_TIME * TRAIN_TT + B_COST * TRAIN_COST + B_HE * TRAIN_HE
SM_SP = ASC_SM  * one + B_TIME * SM_TT + B_COST * SM_COST + B_HE * SM_HE
V = {3: Car_SP,1: SBB_SP,2: SM_SP}
av = {3: CAR_AV_SP,1: TRAIN_AV_SP,2: SM_AV}

UTILITY1= ASC_1*one+B_DIRECT_NEXT*Direct_next+B_PEOPLE_AROUND*Pelple_around+ B_WINDOWWALL*Window/wall+ B_DISTANCE* Distance_to_exit+B_24SEAT* two_or_4seat+B_AGE*Age+B_GENDER*Gender
for i in range(1, 41):
    globals()['UTILITY_%s' % i] = globals()['ASC_%s' % i]*one+ B_DIRECT_NEXT* globals()['Direct_next_%s' % i]+ B_PEOPLE_AROUND* globals()['People_around_%s' % i]+B_WINDOWWALL* globals()['Window/wall_%s' % i]+ B_DISTANCE*globals()['Distance_to_exit_%s' % i]+B_24SEAT*globals()['two_or4seat_%s' % i]+ B_AGE*Age+B_GENDER*Gender

V = {1: UTILITY_1, 2: UTILITY_2, 3: UTILITY_3, 1: UTILITY_1, 2: UTILITY_2, 3: UTILITY_3, 4: UTILITY_4, 5: UTILITY_5, 6: UTILITY_6, 7: UTILITY_7,
    8: UTILITY_8, 9: UTILITY_9, 10: UTILITY_10, 11: UTILITY_11, 12: UTILITY_12, 13: UTILITY_13, 14: UTILITY_14, 15: UTILITY_15, 16: UTILITY_16,
    17: UTILITY_17, 18: UTILITY_18, 19: UTILITY_19, 20: UTILITY_20, 21: UTILITY_21, 22: UTILITY_22, 23: UTILITY_23, 24: UTILITY_24, 25: UTILITY_25,
    26: UTILITY_26, 27: UTILITY_27, 28: UTILITY_28, 29: UTILITY_29, 30: UTILITY_30, 31: UTILITY_31, 32: UTILITY_32, 33: UTILITY_33, 34: UTILITY_34,
    35: UTILITY_35, 36: UTILITY_36, 37: UTILITY_17, 38: UTILITY_38, 39: UTILITY_39, 40: UTILITY_40 }
av = {1:SEATAV_1, 2:SEATAV_2, 3:SEATAV_3, 4:SEATAV_4, 5:SEATAV_5, 6:SEATAV_6, 7:SEATAV_7, 8:SEATAV_8, 9:SEATAV_9, 10:SEATAV_10,
    11:SEATAV_11, 12:SEATAV_12, 13:SEATAV_13, 14:SEATAV_14, 15:SEATAV_15, 16:SEATAV_16, 17:SEATAV_17, 18:SEATAV_18, 19:SEATAV_19, 20:SEATAV_20,
    21:SEATAV_21, 22:SEATAV_22, 23:SEATAV_23, 24:SEATAV_24, 25:SEATAV_25, 26:SEATAV_26, 27:SEATAV_27, 28:SEATAV_28, 29:SEATAV_29, 30:SEATAV_30,
    31:SEATAV_31, 32:SEATAV_32, 13:SEATAV_33, 34:SEATAV_34, 35:SEATAV_35, 36:SEATAV_36, 37:SEATAV_37, 38:SEATAV_38, 39:SEATAV_39, 40:SEATAV_40,}
#Exclude
#BIOGEME_OBJECT.EXCLUDE = (((  PURPOSE   !=  1  ) * (  PURPOSE   !=  3  )) + (  CHOICE   ==  0  ))>0

# MNL (Multinomial Logit model), with availability conditions
prob = bioLogit(V,av,Choice)
l = log(prob)

# Defines an iterator on the data
rowIterator('obsIter') 

# Define the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(l,'obsIter')

# Optimization algorithm
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"

# Print some statistics:
nullLoglikelihood(av,'obsIter')
choiceSet = [i+1 for i in range(40)] #Change choice set to 40
cteLoglikelihood(choiceSet,Choice,'obsIter')
availabilityStatistics(av,'obsIter')
for i in range(1,41):
    BIOGEME_OBJECT.FORMULAS[f'Utility_{i}'] = globals()['UTILITY_%s' % i]
