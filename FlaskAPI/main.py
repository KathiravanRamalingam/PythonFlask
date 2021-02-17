from flask import Flask, request, render_template , make_response, jsonify
import datetime
app = Flask(__name__)


def CheapPaymentGateway():
    print("Cheap Payment Gateway is working ")

def ExpensivePaymentGateway():
    print("Expensive Payment Gateway is working ")


def PremiumPaymentGateway():
    print("Premium Payment Gateway is working ")
    

@app.route('/', methods=['GET','POST'])
def ProcessPayment():
    if request.method == 'POST':
        name = request.form.get('name',None)
        number=request.form.get('number',None)
        date=request.form.get('date',None)
        #ct ,the Variable refers to CURRENT DATE 
        ct = datetime.datetime.now()
        #d1 ,the Variable refers to CARD EXPIRATION DATE
        d1 = datetime.datetime.strptime(date,'%m/%Y')
        #print(ct<d1)
        amount = int(request.form.get('amount',None))
        code=request.form.get('code',None)
        if amount > 0 and amount <=20:
            CheapPaymentGateway()
        elif amount >20 and amount <= 500:
            ExpensivePaymentGateway()
        else:
            PremiumPaymentGateway()

        if not name:
            return make_response(jsonify('400 Bad Request '),400)

        elif not number:
            return make_response(jsonify('400 Bad Request '),400)
        
        elif not date:
            return make_response(jsonify('400 Bad Request '),400)

        elif not code:
            return make_response(jsonify('400 Bad Request '),400)

        elif len(code)>3:
            return make_response(jsonify('400 Bad Request '),400)

        elif not amount:
            return make_response(jsonify('400 Bad Request '),400)
        elif (ct>d1):
            return make_response(jsonify('400 Bad Request '),400)


        else:
            return make_response(jsonify('200 OK'),200)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
    #if we run without the debug=True
    #in case if we have any error in the program then the server automatically shows the "500 Internal Server Error"
