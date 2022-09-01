from Utils.Indicators import Indicators as ind

class ConditionChecker:


    @staticmethod
    def evaluate(yar,conditions):
        result = []
        for i in conditions:
            operand1 = 0
            operand2 = i['value']
            operand = i['operand']
            operatorVar = i['operator']
            if(operand=='Close'):
                operand1 = yar['Close'][-1]
            elif(operand=='RSI'):
                operand1 = ind.RSIUtil(yar['Close'])
            elif(operand=='ADX'):
                operand1 = ind.ADXUtil(yar['High'],yar['Low'],yar['Close'])
            if(str(operand1)=='nan'):
                result.append(False)
                continue
            # print(operand1)
            result.append(ConditionChecker.evalOperator(operand1,operand2,operatorVar))
        # print(result)
        count  = 0
        for i in result:
            if(i==False):
                count+=1
        # print(count)
        if(len(result)>0 and count==0):
            return True
        else:
            return False
    
    @staticmethod
    def evalOperator(operand1,operand2,operator):
        if(operator=='<'):
            if(operand1<operand2):
                return True
            else:
                return False
        elif(operator=='<='):
            if(operand1<=operand2):
                return True
            else:
                return False
        elif(operator=='>'):
            if(operand1>operand2):
                return True
            else:
                return False
        elif(operator=='>='):
            if(operand1>=operand2):
                return True
            else:
                return False
        elif(operator=='=='):
            if(operand1==operand2):
                return True
            else:
                return False