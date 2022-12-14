from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class sign(models.Model):
    sid = models.AutoField(('SID'), primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    conformpassword = models.CharField(max_length=100)

    def __str__(self):
        return self.email + " " + self.password

    class meta:
        db_table = "sign"


class company(models.Model):
    cid = models.AutoField(('CID'), primary_key=True)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100)
    caddress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    cemail = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    cimg = models.ImageField(upload_to='images/', default='/images/default.png')
    bname = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    ctype = models.CharField(max_length=100)
    abt = models.CharField(max_length=100)
    paid = models.CharField(max_length=100)


class customer(models.Model):
    customerid = models.AutoField(('CUSTID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    gsttype = models.CharField(max_length=100, null=True)
    gstin = models.CharField(max_length=100, default='')
    panno = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    shipstreet = models.CharField(max_length=100, null=True)
    shipcity = models.CharField(max_length=100, null=True)
    shipstate = models.CharField(max_length=100, null=True)
    shippincode = models.CharField(max_length=100, null=True)
    shipcountry = models.CharField(max_length=100, null=True)

    class meta:
        db_table = "customer"


class supplier(models.Model):
    supplierid = models.AutoField(('SUPPLIERID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    billingrate = models.CharField(max_length=100)
    terms = models.CharField(max_length=100)
    addterms = models.CharField(max_length=100)
    openingbalance = models.CharField(max_length=100)
    accountno = models.CharField(max_length=100)
    gsttype = models.CharField(max_length=100)
    gstin = models.CharField(max_length=100)
    taxregistrationno = models.CharField(max_length=100)
    effectivedate = models.CharField(max_length=100)
    defaultexpenceaccount = models.CharField(max_length=100)
    tds = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)


class advancepayment(models.Model):
    advancepaymentid = models.AutoField(('ADVANCEPAYMENTID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    payee = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    paymentdate = models.CharField(max_length=100)
    refno = models.CharField(max_length=100)
    memo = models.CharField(max_length=100)


class paydowncreditcard(models.Model):
    paycreditcardid = models.AutoField(('PAYCREDITCARDID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    ccno = models.CharField(max_length=100)
    payee = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    dateofpayment = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)


class salesrecpts(models.Model):
    salesrecptsid = models.AutoField(('SALESRECPTID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    salename = models.CharField(max_length=100)
    saleemail = models.EmailField()
    saleaddress = models.CharField(max_length=150)
    saledate = models.CharField(max_length=10)
    saleno = models.CharField(max_length=20)
    salesplace = models.CharField(max_length=100)
    salepay = models.CharField(max_length=10)
    salerefno = models.CharField(max_length=10)
    saledeposit = models.CharField(max_length=150)
    salepro = models.CharField(max_length=100)
    salehsn = models.CharField(max_length=100)
    saledescription = models.CharField(max_length=100)
    saleqty = models.CharField(max_length=100)
    saleprice = models.CharField(max_length=100)
    saaletotal = models.CharField(max_length=100)
    salesubtotal = models.CharField(max_length=100)
    tax = models.IntegerField(default=0, null=True)
    saletaxamount = models.CharField(max_length=100)
    salegrandtotal = models.CharField(max_length=100)

    category2 = models.CharField(max_length=100)
    categoryhsn2 = models.CharField(max_length=100)
    descrptin2 = models.CharField(max_length=100)
    catqty2 = models.CharField(max_length=100)
    catprice2 = models.CharField(max_length=100)
    cattotal2 = models.CharField(max_length=100)
    tax1 = models.IntegerField(default=0, null=True)

    category3 = models.CharField(max_length=100)
    categoryhsn3 = models.CharField(max_length=100)
    descrptin3 = models.CharField(max_length=100)
    catqty3 = models.CharField(max_length=100)
    catprice3 = models.CharField(max_length=100)
    cattotal3 = models.CharField(max_length=100)
    tax2 = models.IntegerField(default=0, null=True)

    category4 = models.CharField(max_length=100)
    categoryhsn4 = models.CharField(max_length=100)
    descrptin4 = models.CharField(max_length=100)
    catqty4 = models.CharField(max_length=100)
    catprice4 = models.CharField(max_length=100)
    cattotal4 = models.CharField(max_length=100)
    tax3 = models.IntegerField(default=0, null=True)
    offline = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return self.saleno


class timeact(models.Model):
    timeactid = models.AutoField(('TIMEACTID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    timdate = models.CharField(max_length=10)
    timename = models.CharField(max_length=20)
    timecust = models.CharField(max_length=20)
    timecheck = models.CharField(max_length=10)
    timebill = models.CharField(max_length=20)
    timecheckk = models.CharField(max_length=10)
    timestart = models.CharField(max_length=6)
    timeend = models.CharField(max_length=6)
    tyme = models.CharField(max_length=6)
    timedes = models.CharField(max_length=50)


class timeactsale(models.Model):
    timeactsaleid = models.AutoField(('TIMEACTSALEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    timdatesale = models.CharField(max_length=10)
    timenamesale = models.CharField(max_length=20)
    timecustsale = models.CharField(max_length=20)
    timechecksale = models.CharField(max_length=10)
    timebillsale = models.CharField(max_length=20)
    timecheckksale = models.CharField(max_length=10)
    timestartsale = models.CharField(max_length=6)
    timeendsale = models.CharField(max_length=6)
    tymesale = models.CharField(max_length=6)
    timedessale = models.CharField(max_length=50)


class Cheqs(models.Model):
    chequeid = models.AutoField(('CHEQUEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    payee = models.CharField(max_length=100)
    bankacc = models.CharField(max_length=100)
    mailaddr = models.CharField(max_length=100)
    paydate = models.CharField(max_length=100)
    chequeno = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    category1 = models.CharField(max_length=100)
    descrptin1 = models.CharField(max_length=100)
    catqty1 = models.CharField(max_length=100)
    catprice1 = models.CharField(max_length=100)
    cattotal1 = models.CharField(max_length=100)

    category2 = models.CharField(max_length=100)
    descrptin2 = models.CharField(max_length=100)
    catqty2 = models.CharField(max_length=100)
    catprice2 = models.CharField(max_length=100)
    cattotal2 = models.CharField(max_length=100)

    category3 = models.CharField(max_length=100)
    descrptin3 = models.CharField(max_length=100)
    catqty3 = models.CharField(max_length=100)
    catprice3 = models.CharField(max_length=100)
    cattotal3 = models.CharField(max_length=100)

    category4 = models.CharField(max_length=100)
    descrptin4 = models.CharField(max_length=100)
    catqty4 = models.CharField(max_length=100)
    catprice4 = models.CharField(max_length=100)
    cattotal4 = models.CharField(max_length=100)

    product = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='')
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    product2 = models.CharField(max_length=100)
    hsn2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=100)
    qty2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    total2 = models.CharField(max_length=100)
    product3 = models.CharField(max_length=100)
    hsn3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=100)
    qty3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    total3 = models.CharField(max_length=100)
    product4 = models.CharField(max_length=100)
    hsn4 = models.CharField(max_length=100)
    description4 = models.CharField(max_length=100)
    qty4 = models.CharField(max_length=100)
    price4 = models.CharField(max_length=100)
    total4 = models.CharField(max_length=100)

    subtotal = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    tax2 = models.CharField(max_length=100, default='')
    tax3 = models.CharField(max_length=100, default='')
    tax4 = models.CharField(max_length=100, default='')
    taxamount = models.CharField(max_length=100)
    grandtotal = models.CharField(max_length=100)


class invoice(models.Model):
    invoiceid = models.AutoField(('INVOICEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    customername = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    invoiceno = models.IntegerField(default=1000)
    terms = models.CharField(max_length=100, default='')
    invoicedate = models.CharField(max_length=100)
    duedate = models.CharField(max_length=100)
    bname = models.CharField(max_length=255, default='')
    placosupply = models.CharField(max_length=100, default='')
    product = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='')
    qty = models.IntegerField(default=0, null=True)
    price = models.CharField(max_length=100)
    total = models.IntegerField(default=0, null=True)
    tax = models.CharField(max_length=100)
    subtotal = models.IntegerField(default=0, null=True)
    grandtotal = models.IntegerField(default=0, null=True)
    product2 = models.CharField(max_length=100, default='')
    hsn2 = models.CharField(max_length=100, default='')
    description2 = models.CharField(max_length=100, default='')
    qty2 = models.IntegerField(default=0, null=True)
    price2 = models.CharField(max_length=100, default='')
    total2 = models.IntegerField(default=0, null=True)
    tax2 = models.CharField(max_length=100, default='')
    product3 = models.CharField(max_length=100, default='')
    hsn3 = models.CharField(max_length=100, default='')
    description3 = models.CharField(max_length=100, default='')
    qty3 = models.IntegerField(default=0, null=True)
    price3 = models.CharField(max_length=100, default='')
    total3 = models.IntegerField(default=0, null=True)
    tax3 = models.CharField(max_length=100, default='')
    product4 = models.CharField(max_length=100, default='')
    hsn4 = models.CharField(max_length=100, default='')
    description4 = models.CharField(max_length=100, default='')
    qty4 = models.IntegerField(default=0, null=True)
    price4 = models.CharField(max_length=100, default='')
    total4 = models.IntegerField(default=0, null=True)
    tax4 = models.CharField(max_length=100, default='')
    amtrecvd = models.IntegerField(default=0, null=True)
    taxamount = models.IntegerField(default=0, null=True)
    baldue = models.CharField(max_length=100, default='')


class bills(models.Model):
    billid = models.AutoField(('BILLID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    payee = models.CharField(max_length=100)
    paymacnt = models.CharField(max_length=100)
    paymdate = models.CharField(max_length=100)
    paymmethod = models.CharField(max_length=100)
    refno = models.CharField(max_length=100)
    totamt = models.CharField(max_length=100)

    category1 = models.CharField(max_length=100)
    descrptin1 = models.CharField(max_length=100)
    catqty1 = models.CharField(max_length=100)
    catprice1 = models.CharField(max_length=100)
    cattotal1 = models.CharField(max_length=100)

    category2 = models.CharField(max_length=100)
    descrptin2 = models.CharField(max_length=100)
    catqty2 = models.CharField(max_length=100)
    catprice2 = models.CharField(max_length=100)
    cattotal2 = models.CharField(max_length=100)

    category3 = models.CharField(max_length=100)
    descrptin3 = models.CharField(max_length=100)
    catqty3 = models.CharField(max_length=100)
    catprice3 = models.CharField(max_length=100)
    cattotal3 = models.CharField(max_length=100)

    category4 = models.CharField(max_length=100)
    descrptin4 = models.CharField(max_length=100)
    catqty4 = models.CharField(max_length=100)
    catprice4 = models.CharField(max_length=100)
    cattotal4 = models.CharField(max_length=100)

    product = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    product2 = models.CharField(max_length=100)
    hsn2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=100)
    qty2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    total2 = models.CharField(max_length=100)
    product3 = models.CharField(max_length=100)
    hsn3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=100)
    qty3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    total3 = models.CharField(max_length=100)
    product4 = models.CharField(max_length=100)
    hsn4 = models.CharField(max_length=100)
    description4 = models.CharField(max_length=100)
    qty4 = models.CharField(max_length=100)
    price4 = models.CharField(max_length=100)
    total4 = models.CharField(max_length=100)

    subtotal = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    tax2 = models.CharField(max_length=100, default='')
    tax3 = models.CharField(max_length=100, default='')
    tax4 = models.CharField(max_length=100, default='')
    taxamount = models.CharField(max_length=100)
    grandtotal = models.CharField(max_length=100)
    payornot = models.CharField(max_length=100, default='', null=True)


class addac(models.Model):
    acname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    dateadded = models.DateField(max_length=100, default='')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class suplrcredit(models.Model):
    suppliercreditid = models.AutoField(('SUPCREDITID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    supplier = models.CharField(max_length=100)
    mailaddr = models.CharField(max_length=100)
    paymdate = models.CharField(max_length=100)
    refno = models.CharField(max_length=100)
    ccatego = models.CharField(max_length=100)
    cdescrip = models.CharField(max_length=100)
    cqty = models.CharField(max_length=100)
    cprice = models.CharField(max_length=100)
    ctotal = models.CharField(max_length=100)
    ccatego2 = models.CharField(max_length=100)
    cdescrip2 = models.CharField(max_length=100)
    cqty2 = models.CharField(max_length=100)
    cprice2 = models.CharField(max_length=100)
    ctotal2 = models.CharField(max_length=100)
    ccatego3 = models.CharField(max_length=100)
    cdescrip3 = models.CharField(max_length=100)
    cqty3 = models.CharField(max_length=100)
    cprice3 = models.CharField(max_length=100)
    ctotal3 = models.CharField(max_length=100)
    ccatego4 = models.CharField(max_length=100)
    cdescrip4 = models.CharField(max_length=100)
    cqty4 = models.CharField(max_length=100)
    cprice4 = models.CharField(max_length=100)
    ctotal4 = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='')
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    product2 = models.CharField(max_length=100)
    hsn2 = models.CharField(max_length=100)
    description2 = models.CharField(max_length=100)
    qty2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    total2 = models.CharField(max_length=100)
    product3 = models.CharField(max_length=100)
    hsn3 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=100)
    qty3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    total3 = models.CharField(max_length=100)
    product4 = models.CharField(max_length=100)
    hsn4 = models.CharField(max_length=100)
    description4 = models.CharField(max_length=100)
    qty4 = models.CharField(max_length=100)
    price4 = models.CharField(max_length=100)
    total4 = models.CharField(max_length=100)

    subtotal = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    tax2 = models.CharField(max_length=100, default='')
    tax3 = models.CharField(max_length=100, default='')
    tax4 = models.CharField(max_length=100, default='')
    taxamount = models.CharField(max_length=100)
    grandtotal = models.CharField(max_length=100)
    creditamount = models.CharField(max_length=100)


class credit(models.Model):
    creditnoteid = models.AutoField(('CREDITNOTEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    biladdr = models.CharField(max_length=100)
    creditdate = models.CharField(max_length=100)
    creditno = models.CharField(max_length=100, default='')
    place = models.CharField(max_length=100)
    invnum = models.CharField(max_length=100)
    invperiod = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    descrip = models.CharField(max_length=100)
    qty = models.IntegerField(default=0, null=True)
    price = models.CharField(max_length=100)
    tax = models.CharField(max_length=100, default='0')
    subtot = models.IntegerField(default=0, null=True)
    total = models.IntegerField(default=0, null=True)
    grndtot = models.IntegerField(default=0, null=True)
    taxamnt = models.IntegerField(default=0, null=True)
    product1 = models.CharField(max_length=100, default='')
    descrip1 = models.CharField(max_length=100, default='')
    qty1 = models.IntegerField(default=0, null=True)
    price1 = models.CharField(max_length=100, default='')
    tax1 = models.CharField(max_length=100, default='0')
    total1 = models.IntegerField(default=0, null=True)
    product2 = models.CharField(max_length=100, default='')
    descrip2 = models.CharField(max_length=100, default='')
    qty2 = models.IntegerField(default=0, null=True)
    price2 = models.CharField(max_length=100, default='')
    tax2 = models.CharField(max_length=100, default='0')
    total2 = models.IntegerField(default=0, null=True)
    product3 = models.CharField(max_length=100, default='')
    descrip3 = models.CharField(max_length=100, default='')
    qty3 = models.IntegerField(default=0, null=True)
    price3 = models.CharField(max_length=100, default='')
    total3 = models.IntegerField(default=0, null=True)
    tax3 = models.CharField(max_length=100, default='0')

    class meta:
        db_table = "credit"


class payment(models.Model):
    paymentid = models.AutoField(('PAYMENTID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    findinvoice = models.CharField(max_length=100, null=True)
    paymdate = models.CharField(max_length=100)
    pmethod = models.CharField(max_length=100)
    refno = models.CharField(max_length=100)
    depto = models.CharField(max_length=100)
    amtreceived = models.CharField(max_length=100)
    descrip = models.CharField(max_length=100, default='')
    duedate = models.CharField(max_length=10, default='')
    orgamt = models.CharField(max_length=100, default='0')
    openbal = models.CharField(max_length=100, default='0')
    payment = models.CharField(max_length=100, default='0')
    amtapply = models.CharField(max_length=100, default='0')
    amtcredit = models.CharField(max_length=100, default='0')
    descrip1 = models.CharField(max_length=100, default='')
    duedate1 = models.CharField(max_length=10, default='')
    orgamt1 = models.CharField(max_length=100, default='')
    openbal1 = models.CharField(max_length=100, default='')
    payment1 = models.CharField(max_length=100, default='0')
    descrip2 = models.CharField(max_length=100, default='')
    duedate2 = models.CharField(max_length=10, default='')
    orgamt2 = models.CharField(max_length=100, default='')
    openbal2 = models.CharField(max_length=100, default='')
    payment2 = models.CharField(max_length=100, default='0')
    descrip3 = models.CharField(max_length=100, default='')
    duedate3 = models.CharField(max_length=10, default='')
    orgamt3 = models.CharField(max_length=100, default='')
    openbal3 = models.CharField(max_length=100, default='')
    payment3 = models.CharField(max_length=100, default='0')
    descrip4 = models.CharField(max_length=100, default='')
    duedate4 = models.CharField(max_length=10, default='')
    orgamt4 = models.CharField(max_length=100, default='0')
    openbal4 = models.CharField(max_length=100, default='0')
    payment4 = models.CharField(max_length=100, default='0')
    descrip5 = models.CharField(max_length=100, default='')
    duedate5 = models.CharField(max_length=10, default='')
    orgamt5 = models.CharField(max_length=100, default='0')
    openbal5 = models.CharField(max_length=100, default='0')
    payment5 = models.CharField(max_length=100, default='0')
    descrip6 = models.CharField(max_length=100, default='')
    duedate6 = models.CharField(max_length=10, default='')
    orgamt6 = models.CharField(max_length=100, default='0')
    openbal6 = models.CharField(max_length=100, default='0')
    payment6 = models.CharField(max_length=100, default='0')
    descrip7 = models.CharField(max_length=100, default='')
    duedate7 = models.CharField(max_length=10, default='')
    orgamt7 = models.CharField(max_length=100, default='0')
    openbal7 = models.CharField(max_length=100, default='0')
    payment7 = models.CharField(max_length=100, default='0')
    descrip8 = models.CharField(max_length=100, default='')
    duedate8 = models.CharField(max_length=10, default='')
    orgamt8 = models.CharField(max_length=100, default='0')
    openbal8 = models.CharField(max_length=100, default='0')
    payment8 = models.CharField(max_length=100, default='0')
    descrip9 = models.CharField(max_length=100, default='')
    duedate9 = models.CharField(max_length=10, default='')
    orgamt9 = models.CharField(max_length=100, default='0')
    openbal9 = models.CharField(max_length=100, default='0')
    payment9 = models.CharField(max_length=100, default='0')

    class meta:
        db_table = "payment"


class expences(models.Model):
    expencesid = models.AutoField(('EXPENCEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    payee = models.CharField(max_length=100)
    paymdate = models.CharField(max_length=100)
    paymmethod = models.CharField(max_length=100)
    refno = models.CharField(max_length=100)
    totamt = models.CharField(max_length=100)

    category1 = models.CharField(max_length=100)
    descrptin1 = models.CharField(max_length=100)
    catqty1 = models.CharField(max_length=100)
    catprice1 = models.CharField(max_length=100)
    cattotal1 = models.CharField(max_length=100)

    category2 = models.CharField(max_length=100)
    descrptin2 = models.CharField(max_length=100)
    catqty2 = models.CharField(max_length=100)
    catprice2 = models.CharField(max_length=100)
    cattotal2 = models.CharField(max_length=100)

    category3 = models.CharField(max_length=100)
    descrptin3 = models.CharField(max_length=100)
    catqty3 = models.CharField(max_length=100)
    catprice3 = models.CharField(max_length=100)
    cattotal3 = models.CharField(max_length=100)

    category4 = models.CharField(max_length=100)
    descrptin4 = models.CharField(max_length=100)
    catqty4 = models.CharField(max_length=100)
    catprice4 = models.CharField(max_length=100)
    cattotal4 = models.CharField(max_length=100)

    product = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    product2 = models.CharField(max_length=100, default=' ')
    hsn2 = models.CharField(max_length=100, default=' ')
    description2 = models.CharField(max_length=100, default=' ')
    qty2 = models.CharField(max_length=100, default=' ')
    price2 = models.CharField(max_length=100, default=' ')
    total2 = models.CharField(max_length=100, default=' ')
    product3 = models.CharField(max_length=100, default=' ')
    hsn3 = models.CharField(max_length=100, default=' ')
    description3 = models.CharField(max_length=100, default=' ')
    qty3 = models.CharField(max_length=100, default=' ')
    price3 = models.CharField(max_length=100, default=' ')
    total3 = models.CharField(max_length=100, default=' ')
    product4 = models.CharField(max_length=100, default=' ')
    hsn4 = models.CharField(max_length=100, default=' ')
    description4 = models.CharField(max_length=100, default=' ')
    qty4 = models.CharField(max_length=100, default=' ')
    price4 = models.CharField(max_length=100, default=' ')
    total4 = models.CharField(max_length=100, default=' ')

    subtotal = models.CharField(max_length=100, default=' ')
    tax = models.CharField(max_length=100, default=' ')
    tax2 = models.CharField(max_length=100, default=' ')
    tax3 = models.CharField(max_length=100, default=' ')
    tax4 = models.CharField(max_length=100, default=' ')
    taxamount = models.CharField(max_length=100, default=' ')
    grandtotal = models.CharField(max_length=100, default=' ')

    class meta:
        db_table = "expences"






class delayedcharge(models.Model):
    delayedchargeid = models.AutoField(('DELAYEDCHARGEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    delayedchargedate = models.CharField(max_length=100)
    delayedchargeno = models.CharField(max_length=100)
    prodorser = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    tax = models.CharField(max_length=100, default='0')
    total = models.CharField(max_length=100)
    subtotal = models.CharField(max_length=100, default='')
    grandtotal = models.CharField(max_length=100, default='')
    prodorser1 = models.CharField(max_length=100, default='')
    description1 = models.CharField(max_length=100, default='')
    qty1 = models.CharField(max_length=100, default='')
    rate1 = models.CharField(max_length=100, default='')
    total1 = models.CharField(max_length=100, default='')
    tax1 = models.CharField(max_length=100, default='0')
    prodorser2 = models.CharField(max_length=100, default='')
    description2 = models.CharField(max_length=100, default='')
    qty2 = models.CharField(max_length=100, default='')
    rate2 = models.CharField(max_length=100, default='')
    total2 = models.CharField(max_length=100, default='')
    tax2 = models.CharField(max_length=100, default='0')
    prodorser3 = models.CharField(max_length=100, default='')
    description3 = models.CharField(max_length=100, default='')
    qty3 = models.CharField(max_length=100, default='')
    rate3 = models.CharField(max_length=100, default='')
    total3 = models.CharField(max_length=100, default='')
    tax3 = models.CharField(max_length=100, default='0')
    taxamount = models.CharField(max_length=100, default='')


class service(models.Model):
    serviceid = models.AutoField(('SERVICEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="img/%y")
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    sac = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    categ = models.CharField(max_length=100)
    descr = models.CharField(max_length=100)
    saleprice = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    abatement = models.CharField(max_length=100)
    sertype = models.CharField(max_length=100)
    purchasedescr = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    expenseaccount = models.CharField(max_length=100)
    purchasetax = models.CharField(max_length=100)
    revcharge = models.CharField(max_length=100)
    presupplier = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class noninventory(models.Model):
    noninventoryid = models.AutoField(('NONINVENTORYID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/%y")
    name = models.CharField(max_length=100, null=True)
    sku = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    descr = models.CharField(max_length=100)
    saleprice = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    purchasedescr = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    expenseaccount = models.CharField(max_length=100)
    purchasetax = models.CharField(max_length=100)
    revcharge = models.CharField(max_length=100)
    presupplier = models.CharField(max_length=100)
    qty = models.CharField(max_length=100, default='0')


def _str_(self):
    return self.name


class bundle(models.Model):
    bundleid = models.AutoField(('BUNDLEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/%y")
    # image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    product1 = models.CharField(max_length=100, default="", null=True)
    product2 = models.CharField(max_length=100, default="", null=True)
    product3 = models.CharField(max_length=100, default="", null=True)
    product4 = models.CharField(max_length=100, default="", null=True)
    hsn1 = models.CharField(max_length=100, default="", null=True)
    hsn2 = models.CharField(max_length=100, default="", null=True)
    hsn3 = models.CharField(max_length=100, default="", null=True)
    hsn4 = models.CharField(max_length=100, default="", null=True)
    description1 = models.CharField(max_length=255, default="", null=True)
    description2 = models.CharField(max_length=255, default="", null=True)
    description3 = models.CharField(max_length=255, default="", null=True)
    description4 = models.CharField(max_length=255, default="", null=True)
    qty1 = models.IntegerField(default=0, null=True)
    qty2 = models.IntegerField(default=0, null=True)
    qty3 = models.IntegerField(default=0, null=True)
    qty4 = models.IntegerField(default=0, null=True)
    price1 = models.FloatField(default=0.0, null=True)
    price2 = models.FloatField(default=0.0, null=True)
    price3 = models.FloatField(default=0.0, null=True)
    price4 = models.FloatField(default=0.0, null=True)
    total1 = models.FloatField(default=0.0, null=True)
    total2 = models.FloatField(default=0.0, null=True)
    total3 = models.FloatField(default=0.0, null=True)
    total4 = models.FloatField(default=0.0, null=True)
    tax1 = models.FloatField(default=0.0, null=True)
    tax2 = models.FloatField(default=0.0, null=True)
    tax3 = models.FloatField(default=0.0, null=True)
    tax4 = models.FloatField(default=0.0, null=True)
    grandtotal = models.FloatField(default=0.0, null=True)

    def _str_(self):
        return self.name


class inventory(models.Model):
    inventoryid = models.AutoField(('INVENTORYID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/%y', default='/images/default.png')
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    initialqty = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    stockalrt = models.CharField(max_length=100)
    invacnt = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    salesprice = models.CharField(max_length=10)
    incomeacnt = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    purchaseinfo = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    expacnt = models.CharField(max_length=100)
    purtax = models.CharField(max_length=100)
    revcharge = models.CharField(max_length=100)
    presupplier = models.CharField(max_length=100)
    cxq = models.FloatField(default=0.0, null=True)

    def __str__(self):
        return self.name


# extra

class ProductModel(models.Model):
    Pid = models.IntegerField(primary_key=True)
    Pname = models.CharField(max_length=100)

    class Meta:
        db_table = "producttable"

    def __str__(self):
        return self.Pname


class ItemModel(models.Model):
    Itemid = models.IntegerField(primary_key=True)
    Itemname = models.CharField(max_length=100)
    Pid = models.IntegerField()

    class Meta:
        db_table = "itemstable"

    def __str__(self):
        return self.Itemname


class accountype(models.Model):
    accountypeid = models.AutoField(('ACCOUNTYPEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    accountname = models.CharField(max_length=100)
    accountbal = models.CharField(max_length=100, default='')


class bankstatement(models.Model):
    bankstatementid = models.AutoField(('BANKSTATEMENTID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    debit = models.FloatField(default=0.0, null=True)
    credit = models.FloatField(default=0.0, null=True)


class accounts(models.Model):
    accountsid = models.AutoField(('ACCOUNTSID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    proid = models.ForeignKey(accountype, on_delete=models.CASCADE)
    productid = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    acctype = models.CharField(max_length=100)
    detype = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    gst = models.CharField(max_length=100, default='', null=True)
    deftaxcode = models.CharField(max_length=100)
    balance = models.FloatField(default=0.0, null=True)
    asof = models.DateField()
    balfordisp = models.FloatField(default=0.0, null=True)


class accounts1(models.Model):
    accounts1id = models.AutoField(('ACCOUNTSID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    acctype = models.CharField(max_length=100)
    detype = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    gst = models.CharField(max_length=100, default='', null=True)
    deftaxcode = models.CharField(max_length=100)
    balance = models.FloatField(default=0.0, null=True)
    asof = models.DateField(null=True)


class expenseaccount(models.Model):
    expenseid = models.AutoField(('EXPENSEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    expaccountypid = models.ForeignKey(accountype, on_delete=models.CASCADE)
    account = models.CharField(max_length=100)
    begbal = models.CharField(max_length=100, default='0')
    endbal = models.CharField(max_length=100, default='0')
    enddate = models.CharField(default=timezone.now, max_length=100, null=True)
    dat = models.CharField(default=timezone.now, max_length=100, null=True)
    serchar = models.CharField(max_length=100, default='0')
    expacc = models.CharField(max_length=100, null=True)
    type1 = models.CharField(max_length=100, null=True, default='Journal')
    memo1 = models.CharField(max_length=100, null=True, default='Service Charge')


class incomeaccount(models.Model):
    incomeid = models.AutoField(('INCOMEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    expenceincomeid = models.ForeignKey(expenseaccount, on_delete=models.CASCADE)
    dat1 = models.CharField(default=timezone.now, max_length=100, null=True)
    intear = models.CharField(max_length=100, default='0')
    incacc = models.CharField(max_length=100, null=True)
    type2 = models.CharField(max_length=100, null=True, default='Deposit')
    memo2 = models.CharField(max_length=100, null=True, default='Interest Earned')


class employee(models.Model):
    employeeid = models.AutoField(('EMPLOYEEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    joiningdate = models.CharField(max_length=100)
    employeenumber = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    providebankdetails = models.CharField(max_length=20)
    bankaccountnumber = models.CharField(max_length=100)
    ifsccode = models.CharField(max_length=100)

    hrareceived = models.CharField(max_length=20)
    totalrentpaid = models.CharField(max_length=100)
    livein = models.CharField(max_length=100)

    applicabletaxregime = models.CharField(max_length=100)
    pannumber = models.CharField(max_length=100)
    aadhaarnumber = models.CharField(max_length=100)
    universalaccountnumber = models.CharField(max_length=100)
    pfaccountnumber = models.CharField(max_length=100)
    epsaccountnumber = models.CharField(max_length=100)
    praccountnumber = models.CharField(max_length=100)
    esinumber = models.CharField(max_length=100)
    esidispensaryname = models.CharField(max_length=100)

    basic = models.CharField(max_length=100, default='')
    da = models.CharField(max_length=100, default='')

    othincome1 = models.CharField(max_length=100, default='')
    othincome2 = models.CharField(max_length=100, default='')
    othincome3 = models.CharField(max_length=100, default='')
    othincome4 = models.CharField(max_length=100, default='')
    othincome5 = models.CharField(max_length=100, default='')

    othamount1 = models.CharField(max_length=100, default='')
    othamount2 = models.CharField(max_length=100, default='')
    othamount3 = models.CharField(max_length=100, default='')
    othamount4 = models.CharField(max_length=100, default='')
    othamount5 = models.CharField(max_length=100, default='')

    provifund = models.CharField(max_length=100, default='')
    proftax = models.CharField(max_length=100, default='')
    esi = models.CharField(max_length=100, default='')
    deduc1 = models.CharField(max_length=100, default='')
    deduc2 = models.CharField(max_length=100, default='')
    deduc3 = models.CharField(max_length=100, default='')
    deduc4 = models.CharField(max_length=100, default='')
    deducamt1 = models.CharField(max_length=100, default='')
    deducamt2 = models.CharField(max_length=100, default='')
    deducamt3 = models.CharField(max_length=100, default='')
    deducamt4 = models.CharField(max_length=100, default='')


class payslip(models.Model):
    payslipid = models.AutoField(('PAYSLIPID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    empname = models.CharField(max_length=100)
    employeenumber = models.CharField(max_length=100)
    desig = models.CharField(max_length=100)
    fper = models.CharField(max_length=100)
    tper = models.CharField(max_length=100)
    paydate = models.CharField(max_length=100)
    basic = models.CharField(max_length=100)
    da = models.CharField(max_length=100)
    ear1 = models.CharField(max_length=100)
    earr1 = models.CharField(max_length=100)
    ear2 = models.CharField(max_length=100)
    earr2 = models.CharField(max_length=100)
    ear3 = models.CharField(max_length=100)
    earr3 = models.CharField(max_length=100)
    ear4 = models.CharField(max_length=100)
    earr4 = models.CharField(max_length=100)
    ear5 = models.CharField(max_length=100)
    earr5 = models.CharField(max_length=100)
    ear6 = models.CharField(max_length=100)
    earr6 = models.CharField(max_length=100)
    ear7 = models.CharField(max_length=100)
    earr7 = models.CharField(max_length=100)

    provi = models.CharField(max_length=100)
    prof = models.CharField(max_length=100)
    esi = models.CharField(max_length=100)

    ded1 = models.CharField(max_length=100)
    dedu1 = models.CharField(max_length=100)
    ded2 = models.CharField(max_length=100)
    dedu2 = models.CharField(max_length=100)
    ded3 = models.CharField(max_length=100)
    dedu3 = models.CharField(max_length=100)
    ded4 = models.CharField(max_length=100)
    dedu4 = models.CharField(max_length=100)
    ded5 = models.CharField(max_length=100)
    dedu5 = models.CharField(max_length=100)
    ded6 = models.CharField(max_length=100)
    dedu6 = models.CharField(max_length=100)

    gros = models.CharField(max_length=100)
    tded = models.CharField(max_length=100)
    netsal = models.CharField(max_length=100)


class recon1(models.Model):
    recon1id = models.AutoField(('RECON1ID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    accounttype = models.CharField(max_length=100)
    beginningbalance = models.CharField(max_length=100)
    endingbalance = models.CharField(max_length=100)
    endingdate = models.CharField(max_length=100)

    edat = models.CharField(default=timezone.now, max_length=100, null=True)
    serchar = models.CharField(max_length=100)
    expacc = models.CharField(max_length=100)
    idat1 = models.CharField(default=timezone.now, max_length=100, null=True)
    intear = models.CharField(max_length=100)
    incacc = models.CharField(max_length=100)


class addtax1(models.Model):
    addtax1id = models.AutoField(('ADDTAX1ID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    taxname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class recordpay(models.Model):
    recordpayid = models.AutoField(('RECORDPAYID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    textname = models.CharField(max_length=100)
    paymentdate = models.CharField(max_length=100)
    recordamount = models.CharField(max_length=100)
    recordmemo = models.CharField(max_length=100)


class customize(models.Model):
    customizeid = models.AutoField(("CUSTOMIZEID"), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='', blank=True)
    template = models.CharField(max_length=255, default='', blank=True)
    pcolour = models.CharField(max_length=255, default='', blank=True)
    scolour = models.CharField(max_length=255, default='', blank=True)
    fonts = models.CharField(max_length=255, default='', blank=True)
    lastedited = models.CharField(default=timezone.now, max_length=255, blank=True)
    selected = models.CharField(max_length=255, default='', blank=True)


# Ananthakrishnan
class estimate(models.Model):
    estimateid = models.AutoField(('ESTIMATEID'), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    billingaddress = models.CharField(max_length=100)
    estimatedate = models.DateField()
    expirationdate = models.DateField()
    estimateno = models.CharField(max_length=100)
    placeofsupply = models.CharField(max_length=100)

    product = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    tax = models.CharField(max_length=100, default='0')
    subtotal = models.CharField(max_length=100)
    estimatetotal = models.CharField(max_length=100)

    product1 = models.CharField(max_length=100, default='')
    hsn1 = models.CharField(max_length=100, default='')
    description1 = models.CharField(max_length=100, default='')
    qty1 = models.CharField(max_length=100, default='')
    rate1 = models.CharField(max_length=100, default='')
    total1 = models.CharField(max_length=100, default='')
    tax1 = models.CharField(max_length=100, default='0')

    product2 = models.CharField(max_length=100, default='')
    hsn2 = models.CharField(max_length=100, default='')
    description2 = models.CharField(max_length=100, default='')
    qty2 = models.CharField(max_length=100, default='')
    rate2 = models.CharField(max_length=100, default='')
    total2 = models.CharField(max_length=100, default='')
    tax2 = models.CharField(max_length=100, default='0')

    product3 = models.CharField(max_length=100, default='')
    hsn3 = models.CharField(max_length=100, default='')
    description3 = models.CharField(max_length=100, default='')
    qty3 = models.CharField(max_length=100, default='')
    rate3 = models.CharField(max_length=100, default='')
    total3 = models.CharField(max_length=100, default='')
    tax3 = models.CharField(max_length=100, default='0')

    taxamount = models.CharField(max_length=100, default='')
    reference_number = models.CharField(max_length=100, default='')
    note = models.TextField()
    IGST = models.CharField(max_length=100)
    CGST  =  models.CharField(max_length=100)
    SGST =  models.CharField(max_length=100)
    TCS =  models.CharField(max_length=100)
    file = models.FileField(upload_to='estimate')

    estimate_status = (
        ('Draft','Draft'),
        ('Approved','Approved'),
        ('Invoice','Invoice'),

    )
    
    status =models.CharField(max_length=150,choices=estimate_status,default='Draft')



    def __str__(self):
        return self.customer

class salesorder(models.Model):

    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    
    salename = models.CharField(max_length=100)
    saleemail = models.EmailField()
    saleaddress = models.CharField(max_length=150)
    saledate = models.DateField()
    shipmentdate =  models.DateField()
    saleno = models.CharField(max_length=20)
    placeofsupply = models.CharField(max_length=100)


    product = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    qty = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    tax = models.CharField(max_length=100, default='0')

    
    product1 = models.CharField(max_length=100, default='')
    hsn1 = models.CharField(max_length=100, default='')
    description1 = models.CharField(max_length=100, default='')
    qty1 = models.CharField(max_length=100, default='')
    rate1 = models.CharField(max_length=100, default='')
    total1 = models.CharField(max_length=100, default='')
    tax1 = models.CharField(max_length=100, default='0')

    product2 = models.CharField(max_length=100, default='')
    hsn2 = models.CharField(max_length=100, default='')
    description2 = models.CharField(max_length=100, default='')
    qty2 = models.CharField(max_length=100, default='')
    rate2 = models.CharField(max_length=100, default='')
    total2 = models.CharField(max_length=100, default='')
    tax2 = models.CharField(max_length=100, default='0')

    product3 = models.CharField(max_length=100, default='')
    hsn3 = models.CharField(max_length=100, default='')
    description3 = models.CharField(max_length=100, default='')
    qty3 = models.CharField(max_length=100, default='')
    rate3 = models.CharField(max_length=100, default='')
    total3 = models.CharField(max_length=100, default='')
    tax3 = models.CharField(max_length=100, default='0')
    taxamount = models.CharField(max_length=100, default='')

    reference_number = models.CharField(max_length=100, default='')
    note = models.TextField()

    subtotal = models.CharField(max_length=100)
    IGST = models.CharField(max_length=100)
    CGST  =  models.CharField(max_length=100)
    SGST =  models.CharField(max_length=100)
    TCS =  models.CharField(max_length=100)
    salestotal = models.CharField(max_length=100)
    
    file = models.FileField(upload_to='sales')

    sale_status = (
        ('Draft','Draft'),
        ('Approved','Approved'),
        ('Sales Order','Sales Order'),

    )
    
    status =models.CharField(max_length=150,choices=sale_status,default='Draft')






# Rahanas -------------

class itemtable(models.Model):
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    hsn = models.CharField(max_length=100)
    tax_reference = models.CharField(max_length=100)
    purchase_cost = models.CharField(max_length=100)
    sales_cost = models.CharField(max_length=100)
    tax_rate = models.CharField(max_length=100)
    acount_pur = models.CharField(max_length=100)
    account_sal = models.CharField(max_length=100)
    pur_desc = models.CharField(max_length=100)
    sale_desc = models.CharField(max_length=100)
    intra_st = models.CharField(max_length=100)
    inter_st = models.CharField(max_length=100)
    inventry = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class unittable(models.Model):
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    unit_symbol = models.CharField(max_length=100)
    name = models.CharField(max_length=100)



class mjournal(models.Model):
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    mj_no = models.CharField(max_length=100)
    ref_no = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    j_type = models.CharField(max_length=100,null=True,blank=True)
    currency = models.CharField(max_length=100)
    account1 = models.CharField(max_length=100)
    desc1 = models.CharField(max_length=100,null=True)
    contact1 = models.CharField(max_length=100,null=True)
    debit1 = models.CharField(max_length=100)
    credit1 = models.CharField(max_length=100)
    account2 = models.CharField(max_length=100)
    desc2 = models.CharField(max_length=100,null=True)
    contact2 = models.CharField(max_length=100,null=True)
    debit2 = models.CharField(max_length=100)
    credit2 = models.CharField(max_length=100)
    attach = models.FileField(upload_to="") 
    s_totaldeb = models.CharField(max_length=100)
    s_totalcre = models.CharField(max_length=100)
    total_deb = models.CharField(max_length=100)
    total_cre = models.CharField(max_length=100)
    difference = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default="DRAFT")


class currencies(models.Model):
    currencyid = models.AutoField(("CURRENCYID"), primary_key=True)
    cid = models.ForeignKey(company, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, default='', blank=True)
    name = models.CharField(max_length=255, default='', blank=True)
    symbol = models.CharField(max_length=255, default='', blank=True)
    decimal_places = models.CharField(max_length=255, default='', blank=True)
    format = models.CharField(max_length=255, default='', blank=True)