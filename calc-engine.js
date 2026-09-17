const fmtINR = n => '₹' + Number(n).toLocaleString('en-IN',{minimumFractionDigits:2,maximumFractionDigits:2});
const fmtNum = n => Number(n).toLocaleString('en-IN',{maximumFractionDigits:2});

// Mapping: CALC key -> HTML file name
const CALC_SLUGS = {
  gst: 'gst-calculator',
  emi: 'emi-calculator',
  sip: 'sip-calculator',
  percentage: 'percentage-calculator',
  age: 'age-calculator',
  bmi: 'bmi-calculator',
  discount: 'discount-calculator',
  simpleInterest: 'simple-interest-calculator',
  compoundInterest: 'compound-interest-calculator',
  fd: 'fd-calculator',
  hra: 'hra-calculator',
  ppf: 'ppf-calculator',
  salary: 'salary-calculator',
  tip: 'tip-calculator',
  unitConverter: 'unit-converter',
  salaryTax: 'income-tax-calculator',
  gratuity: 'gratuity-calculator',
  nps: 'nps-calculator',
  lumpsum: 'lumpsum-calculator',
  cagr: 'cagr-calculator',
  homeLoanEligibility: 'loan-eligibility-calculator',
  carLoan: 'car-loan-emi-calculator',
  personalLoan: 'personal-loan-emi-calculator',
  currency: 'currency-converter',
  temperature: 'temperature-converter',
  bmiKids: 'bmi-kids-calculator',
  calorie: 'calorie-calculator',
  water: 'water-intake-calculator',
  pregnancy: 'pregnancy-due-date-calculator',
  dateDiff: 'date-difference-calculator'
};

// Related calculators mapping (5-6 relevant per calculator)
const RELATED = {
  gst: ['discount','salaryTax','salary','percentage'],
  emi: ['homeLoanEligibility','carLoan','personalLoan','salaryTax'],
  sip: ['lumpsum','cagr','nps','ppf'],
  percentage: ['discount','tip','age','dateDiff'],
  age: ['dateDiff','percentage','pregnancy'],
  bmi: ['bmiKids','calorie','water'],
  discount: ['gst','percentage','tip'],
  simpleInterest: ['compoundInterest','fd','emi'],
  compoundInterest: ['simpleInterest','sip','fd','lumpsum'],
  fd: ['simpleInterest','compoundInterest','ppf','nps'],
  hra: ['salary','salaryTax','gratuity'],
  ppf: ['nps','fd','sip','lumpsum'],
  salary: ['salaryTax','hra','gratuity'],
  tip: ['discount','percentage'],
  unitConverter: ['temperature','currency'],
  salaryTax: ['salary','hra','gratuity'],
  gratuity: ['salary','salaryTax'],
  nps: ['ppf','sip','lumpsum','fd'],
  lumpsum: ['sip','cagr','nps','ppf'],
  cagr: ['sip','lumpsum','compoundInterest'],
  homeLoanEligibility: ['emi','carLoan','personalLoan'],
  carLoan: ['emi','homeLoanEligibility','personalLoan'],
  personalLoan: ['emi','homeLoanEligibility','carLoan'],
  currency: ['unitConverter','temperature'],
  temperature: ['unitConverter','currency'],
  bmiKids: ['bmi','calorie','water'],
  calorie: ['bmi','water','bmiKids'],
  water: ['bmi','calorie','bmiKids'],
  pregnancy: ['age','dateDiff'],
  dateDiff: ['age','percentage']
};

const CALCS = {
  gst: {
    name: 'GST Calculator',
    fields: [
      {k:'amount',l:'Amount (₹)',t:'number',v:1000},
      {k:'rate',l:'GST Rate',t:'select',o:[['5','5%'],['12','12%'],['18','18%'],['28','28%']],v:'18'},
      {k:'type',l:'Type',t:'radio',o:[['add','Add GST'],['remove','Remove GST']],v:'add'}
    ],
    calc: v => {
      const a=+v.amount||0,r=+v.rate;
      let base,gst,total;
      if(v.type==='add'){base=a;gst=base*r/100;total=base+gst;}
      else{total=a;base=total/(1+r/100);gst=total-base;}
      return [['Base Amount',fmtINR(base)],['GST Amount',fmtINR(gst)],['Total Amount',fmtINR(total),true]];
    }
  },
  emi: {
    name: 'EMI Calculator',
    fields: [
      {k:'P',l:'Loan Amount (₹)',t:'number',v:500000},
      {k:'R',l:'Interest Rate (% per year)',t:'number',v:8.5,step:'0.1'},
      {k:'N',l:'Tenure (months)',t:'number',v:60}
    ],
    calc: v => {
      const P=+v.P||0,R=(+v.R||0)/12/100,N=+v.N||1;
      const emi=R===0?P/N:(P*R*Math.pow(1+R,N))/(Math.pow(1+R,N)-1);
      const total=emi*N,interest=total-P;
      return [['Monthly EMI',fmtINR(emi),true],['Total Interest',fmtINR(interest)],['Total Payment',fmtINR(total)]];
    }
  },
  sip: {
    name: 'SIP Calculator',
    fields: [
      {k:'M',l:'Monthly Investment (₹)',t:'number',v:5000},
      {k:'R',l:'Expected Return (% per year)',t:'number',v:12,step:'0.1'},
      {k:'Y',l:'Duration (years)',t:'number',v:10}
    ],
    calc: v => {
      const M=+v.M||0,R=(+v.R||0)/12/100,Y=+v.Y||0,N=Y*12;
      const fv=R===0?M*N:M*((Math.pow(1+R,N)-1)/R)*(1+R);
      const invested=M*N,returns=fv-invested;
      return [['Invested Amount',fmtINR(invested)],['Estimated Returns',fmtINR(returns)],['Total Value',fmtINR(fv),true]];
    }
  },
  percentage: {
    name: 'Percentage Calculator',
    fields: [
      {k:'a',l:'What is X% of Y? (X)',t:'number',v:10},
      {k:'b',l:'(Y)',t:'number',v:500},
      {k:'x',l:'X is what % of Y? (X)',t:'number',v:25},
      {k:'y',l:'(Y)',t:'number',v:200}
    ],
    calc: v => {
      const a=+v.a||0,b=+v.b||0,x=+v.x||0,y=+v.y||1;
      return [['X% of Y',fmtNum(a*b/100)],['X is % of Y',((x/y)*100).toFixed(2)+'%',true]];
    }
  },
  age: {
    name: 'Age Calculator',
    fields: [{k:'dob',l:'Date of Birth',t:'date',v:''}],
    calc: v => {
      if(!v.dob)return [['Enter DOB','—']];
      const dob=new Date(v.dob),now=new Date();
      let y=now.getFullYear()-dob.getFullYear();
      let m=now.getMonth()-dob.getMonth();
      let d=now.getDate()-dob.getDate();
      if(d<0){
        m--;
        const daysInPrevMonth = new Date(now.getFullYear(), now.getMonth(), 0).getDate();
        d += daysInPrevMonth;
      }
      if(m<0){y--;m+=12;}
      const months=y*12+m;
      const days=Math.floor((now-dob)/86400000);
      return [[`${y}y ${m}m ${d}d`,'Your Age',true],['Total Months',months+' months'],['Total Days',fmtNum(days)+' days']];
    }
  },
  bmi: {
    name: 'BMI Calculator',
    fields: [
      {k:'w',l:'Weight (kg)',t:'number',v:70,step:'0.1'},
      {k:'h',l:'Height (cm)',t:'number',v:170}
    ],
    calc: v => {
      const w=+v.w||0,h=+v.h||1;
      const bmi=w/Math.pow(h/100,2);
      let cat='Normal';
      if(bmi<18.5)cat='Underweight';
      else if(bmi<25)cat='Normal';
      else if(bmi<30)cat='Overweight';
      else cat='Obese';
      return [['BMI',bmi.toFixed(2),true],['Category',cat]];
    }
  },
  discount: {
    name: 'Discount Calculator',
    fields: [
      {k:'p',l:'Original Price (₹)',t:'number',v:1000},
      {k:'d',l:'Discount (%)',t:'number',v:20}
    ],
    calc: v => {
      const p=+v.p||0,d=+v.d||0,sav=p*d/100,final=p-sav;
      return [['You Save',fmtINR(sav)],['Final Price',fmtINR(final),true]];
    }
  },
  simpleInterest: {
    name: 'Simple Interest Calculator',
    fields: [
      {k:'P',l:'Principal (₹)',t:'number',v:10000},
      {k:'R',l:'Rate (% per year)',t:'number',v:7.5,step:'0.1'},
      {k:'T',l:'Time (years)',t:'number',v:3}
    ],
    calc: v => {
      const P=+v.P||0,R=+v.R||0,T=+v.T||0;
      const si=P*R*T/100,total=P+si;
      return [['Interest',fmtINR(si)],['Total Amount',fmtINR(total),true]];
    }
  },
  compoundInterest: {
    name: 'Compound Interest Calculator',
    fields: [
      {k:'P',l:'Principal (₹)',t:'number',v:10000},
      {k:'R',l:'Rate (% per year)',t:'number',v:7.5,step:'0.1'},
      {k:'T',l:'Time (years)',t:'number',v:3},
      {k:'N',l:'Compounding / year',t:'select',o:[['1','Yearly'],['2','Half-Yearly'],['4','Quarterly'],['12','Monthly']],v:'1'}
    ],
    calc: v => {
      const P=+v.P||0,R=(+v.R||0)/100,T=+v.T||0,N=+v.N||1;
      const total=P*Math.pow(1+R/N,N*T),ci=total-P;
      return [['Interest',fmtINR(ci)],['Total Amount',fmtINR(total),true]];
    }
  },
  fd: {
    name: 'FD Calculator',
    fields: [
      {k:'P',l:'Deposit Amount (₹)',t:'number',v:100000},
      {k:'R',l:'Interest Rate (% per year)',t:'number',v:7,step:'0.1'},
      {k:'T',l:'Time (years)',t:'number',v:5}
    ],
    calc: v => {
      const P=+v.P||0,R=(+v.R||0)/100,T=+v.T||0;
      const total=P*Math.pow(1+R,T),interest=total-P;
      return [['Interest Earned',fmtINR(interest)],['Maturity Amount',fmtINR(total),true]];
    }
  },
  hra: {
    name: 'HRA Exemption Calculator',
    fields: [
      {k:'basic',l:'Basic Salary (₹/year)',t:'number',v:600000},
      {k:'hra',l:'HRA Received (₹/year)',t:'number',v:240000},
      {k:'rent',l:'Rent Paid (₹/year)',t:'number',v:300000},
      {k:'metro',l:'City',t:'radio',o:[['y','Metro'],['n','Non-Metro']],v:'n'}
    ],
    calc: v => {
      const b=+v.basic||0,h=+v.hra||0,r=+v.rent||0;
      const a=h,bAmt=(v.metro==='y'?0.5:0.4)*b,c=Math.max(0,r-0.1*b);
      const exempt=Math.min(a,bAmt,c);
      return [['Exempt Amount',fmtINR(exempt),true],['Taxable HRA',fmtINR(h-exempt)]];
    }
  },
  ppf: {
    name: 'PPF Calculator',
    fields: [
      {k:'M',l:'Yearly Investment (₹)',t:'number',v:150000},
      {k:'R',l:'Interest Rate (%)',t:'number',v:7.1,step:'0.1'},
      {k:'Y',l:'Duration (years)',t:'number',v:15}
    ],
    calc: v => {
      const M=+v.M||0,R=(+v.R||0)/100,Y=+v.Y||0;
      let total=0;
      for(let i=0;i<Y;i++){total=(total+M)*(1+R);}
      const invested=M*Y,interest=total-invested;
      return [['Total Invested',fmtINR(invested)],['Interest Earned',fmtINR(interest)],['Maturity Amount',fmtINR(total),true]];
    }
  },
  salary: {
    name: 'Salary Calculator',
    fields: [{k:'ctc',l:'Annual CTC (₹)',t:'number',v:600000}],
    calc: v => {
      const ctc=+v.ctc||0;
      const basic=ctc*0.4,pf=basic*0.12,std=50000;
      const taxable=ctc-std;
      let tax=0;
      if(taxable>300000){
        if(taxable<=600000)tax=(taxable-300000)*0.05;
        else if(taxable<=900000)tax=15000+(taxable-600000)*0.1;
        else if(taxable<=1200000)tax=45000+(taxable-900000)*0.15;
        else if(taxable<=1500000)tax=90000+(taxable-1200000)*0.2;
        else tax=150000+(taxable-1500000)*0.3;
      }
      tax*=1.04;
      const monthly=ctc/12,monthlyTax=tax/12,monthlyPf=pf/12;
      const takeHome=monthly-monthlyTax-monthlyPf;
      return [['Monthly Gross',fmtINR(monthly)],['Monthly PF',fmtINR(monthlyPf)],['Monthly Tax',fmtINR(monthlyTax)],['Take Home (Monthly)',fmtINR(takeHome),true]];
    }
  },
  tip: {
    name: 'Tip Calculator',
    fields: [
      {k:'bill',l:'Bill Amount (₹)',t:'number',v:1000},
      {k:'tip',l:'Tip (%)',t:'number',v:10},
      {k:'people',l:'Split Between',t:'number',v:1}
    ],
    calc: v => {
      const b=+v.bill||0,t=+v.tip||0,p=+v.people||1;
      const tipAmt=b*t/100,total=b+tipAmt,per=total/p;
      return [['Tip Amount',fmtINR(tipAmt)],['Total Bill',fmtINR(total)],['Per Person',fmtINR(per),true]];
    }
  },
  unitConverter: {
    name: 'Unit Converter',
    fields: [
      {k:'val',l:'Value',t:'number',v:1},
      {k:'from',l:'From',t:'select',o:[['km','Kilometer'],['mi','Mile'],['m','Meter'],['ft','Feet'],['kg','Kilogram'],['lb','Pound'],['c','Celsius'],['f','Fahrenheit']],v:'km'},
      {k:'to',l:'To',t:'select',o:[['km','Kilometer'],['mi','Mile'],['m','Meter'],['ft','Feet'],['kg','Kilogram'],['lb','Pound'],['c','Celsius'],['f','Fahrenheit']],v:'mi'}
    ],
    calc: v => {
      const val=+v.val||0;
      const conv={
        km:{km:1,mi:0.621371,m:1000,ft:3280.84},
        mi:{km:1.60934,mi:1,m:1609.34,ft:5280},
        m:{km:0.001,mi:0.000621371,m:1,ft:3.28084},
        ft:{km:0.0003048,mi:0.000189394,m:0.3048,ft:1},
        kg:{kg:1,lb:2.20462},
        lb:{kg:0.453592,lb:1},
        c:{c:1,f:v=>v*9/5+32},
        f:{c:v=>(v-32)*5/9,f:1}
      };
      let result=NaN;
      if(conv[v.from]&&conv[v.from][v.to]){
        const f=conv[v.from][v.to];
        result=typeof f==='function'?f(val):val*f;
      }
      return [['Result',isNaN(result)?'Invalid':fmtNum(result),true]];
    }
  },
  salaryTax: {
    name: 'Income Tax Calculator',
    fields: [{k:'income',l:'Annual Income (₹)',t:'number',v:1000000}],
    calc: v => {
      const inc=+v.income||0;
      let old=0,newReg=0;
      if(inc>250000){
        if(inc<=500000)old=(inc-250000)*0.05;
        else if(inc<=1000000)old=12500+(inc-500000)*0.2;
        else old=112500+(inc-1000000)*0.3;
      }
      if(inc>300000){
        if(inc<=600000)newReg=(inc-300000)*0.05;
        else if(inc<=900000)newReg=15000+(inc-600000)*0.1;
        else if(inc<=1200000)newReg=45000+(inc-900000)*0.15;
        else if(inc<=1500000)newReg=90000+(inc-1200000)*0.2;
        else newReg=150000+(inc-1500000)*0.3;
      }
      old*=1.04;newReg*=1.04;
      return [['Old Regime Tax',fmtINR(old)],['New Regime Tax',fmtINR(newReg),true],['Savings with New',fmtINR(old-newReg)]];
    }
  },
  gratuity: {
    name: 'Gratuity Calculator',
    fields: [
      {k:'salary',l:'Last Drawn Salary (₹/month)',t:'number',v:50000},
      {k:'years',l:'Years of Service',t:'number',v:10}
    ],
    calc: v => {
      const s=+v.salary||0,y=+v.years||0;
      const g=15*s*y/26;
      return [['Gratuity Amount',fmtINR(g),true]];
    }
  },
  nps: {
    name: 'NPS Calculator',
    fields: [
      {k:'M',l:'Monthly Contribution (₹)',t:'number',v:5000},
      {k:'Y',l:'Years to Retirement',t:'number',v:25},
      {k:'R',l:'Expected Return (%)',t:'number',v:10,step:'0.1'}
    ],
    calc: v => {
      const M=+v.M||0,Y=+v.Y||0,R=(+v.R||0)/12/100,N=Y*12;
      const fv=R===0?M*N:M*((Math.pow(1+R,N)-1)/R)*(1+R);
      const invested=M*N;
      return [['Invested',fmtINR(invested)],['Total Corpus',fmtINR(fv),true],['60% Annuity',fmtINR(fv*0.6)]];
    }
  },
  lumpsum: {
    name: 'Lumpsum Calculator',
    fields: [
      {k:'P',l:'Investment (₹)',t:'number',v:100000},
      {k:'R',l:'Return (% per year)',t:'number',v:12,step:'0.1'},
      {k:'Y',l:'Duration (years)',t:'number',v:10}
    ],
    calc: v => {
      const P=+v.P||0,R=(+v.R||0)/100,Y=+v.Y||0;
      const fv=P*Math.pow(1+R,Y);
      return [['Invested',fmtINR(P)],['Estimated Returns',fmtINR(fv-P)],['Total Value',fmtINR(fv),true]];
    }
  },
  cagr: {
    name: 'CAGR Calculator',
    fields: [
      {k:'begin',l:'Beginning Value (₹)',t:'number',v:100000},
      {k:'end',l:'Ending Value (₹)',t:'number',v:250000},
      {k:'Y',l:'Years',t:'number',v:5}
    ],
    calc: v => {
      const b=+v.begin||1,e=+v.end||0,Y=+v.Y||1;
      const cagr=(Math.pow(e/b,1/Y)-1)*100;
      return [['CAGR',cagr.toFixed(2)+'%',true],['Absolute Return',(((e-b)/b)*100).toFixed(2)+'%']];
    }
  },
  homeLoanEligibility: {
    name: 'Loan Eligibility Calculator',
    fields: [
      {k:'income',l:'Monthly Income (₹)',t:'number',v:50000},
      {k:'emi',l:'Existing EMIs (₹)',t:'number',v:0},
      {k:'R',l:'Interest Rate (%)',t:'number',v:8.5,step:'0.1'},
      {k:'N',l:'Tenure (years)',t:'number',v:20}
    ],
    calc: v => {
      const inc=+v.income||0,exEmi=+v.emi||0,R=(+v.R||0)/12/100,N=(+v.N||1)*12;
      const maxEmi=inc*0.5-exEmi;
      const loan=maxEmi*((Math.pow(1+R,N)-1)/(R*Math.pow(1+R,N)));
      return [['Max EMI',fmtINR(maxEmi)],['Eligible Loan',fmtINR(loan),true]];
    }
  },
  carLoan: {
    name: 'Car Loan EMI Calculator',
    fields: [
      {k:'P',l:'Loan Amount (₹)',t:'number',v:800000},
      {k:'R',l:'Interest Rate (%)',t:'number',v:9.5,step:'0.1'},
      {k:'N',l:'Tenure (months)',t:'number',v:60}
    ],
    calc: v => {
      const P=+v.P||0,R=(+v.R||0)/12/100,N=+v.N||1;
      const emi=R===0?P/N:(P*R*Math.pow(1+R,N))/(Math.pow(1+R,N)-1);
      return [['Monthly EMI',fmtINR(emi),true],['Total Interest',fmtINR(emi*N-P)],['Total Payment',fmtINR(emi*N)]];
    }
  },
  personalLoan: {
    name: 'Personal Loan EMI Calculator',
    fields: [
      {k:'P',l:'Loan Amount (₹)',t:'number',v:200000},
      {k:'R',l:'Interest Rate (%)',t:'number',v:14,step:'0.1'},
      {k:'N',l:'Tenure (months)',t:'number',v:24}
    ],
    calc: v => {
      const P=+v.P||0,R=(+v.R||0)/12/100,N=+v.N||1;
      const emi=R===0?P/N:(P*R*Math.pow(1+R,N))/(Math.pow(1+R,N)-1);
      return [['Monthly EMI',fmtINR(emi),true],['Total Interest',fmtINR(emi*N-P)],['Total Payment',fmtINR(emi*N)]];
    }
  },
  currency: {
    name: 'Currency Converter',
    fields: [
      {k:'amt',l:'Amount',t:'number',v:100},
      {k:'from',l:'From',t:'select',o:[['INR','INR'],['USD','USD'],['EUR','EUR'],['GBP','GBP']],v:'USD'},
      {k:'to',l:'To',t:'select',o:[['INR','INR'],['USD','USD'],['EUR','EUR'],['GBP','GBP']],v:'INR'}
    ],
    calc: v => {
      const amt=+v.amt||0;
      const rates={INR:1,USD:0.012,EUR:0.011,GBP:0.0095};
      const result=amt/rates[v.from]*rates[v.to];
      return [['Converted',fmtNum(result)+' '+v.to,true],['Note','Approx. rates. Verify with bank before transacting.']];
    }
  },
  temperature: {
    name: 'Temperature Converter',
    fields: [
      {k:'val',l:'Temperature',t:'number',v:100},
      {k:'from',l:'From',t:'select',o:[['C','Celsius'],['F','Fahrenheit'],['K','Kelvin']],v:'C'}
    ],
    calc: v => {
      const val=+v.val||0;
      let c;
      if(v.from==='C')c=val;
      else if(v.from==='F')c=(val-32)*5/9;
      else c=val-273.15;
      return [['Celsius',c.toFixed(2)+'°C'],['Fahrenheit',(c*9/5+32).toFixed(2)+'°F',true],['Kelvin',(c+273.15).toFixed(2)+'K']];
    }
  },
  bmiKids: {
    name: 'BMI Calculator for Kids',
    fields: [
      {k:'w',l:'Weight (kg)',t:'number',v:25},
      {k:'h',l:'Height (cm)',t:'number',v:120},
      {k:'age',l:'Age (years)',t:'number',v:8}
    ],
    calc: v => {
      const w=+v.w||0,h=+v.h||1;
      const bmi=w/Math.pow(h/100,2);
      return [['BMI',bmi.toFixed(2),true],['Note','Consult pediatrician for interpretation']];
    }
  },
  calorie: {
    name: 'Calorie Calculator',
    fields: [
      {k:'w',l:'Weight (kg)',t:'number',v:70},
      {k:'h',l:'Height (cm)',t:'number',v:170},
      {k:'age',l:'Age (years)',t:'number',v:25},
      {k:'gender',l:'Gender',t:'radio',o:[['m','Male'],['f','Female']],v:'m'}
    ],
    calc: v => {
      const w=+v.w||0,h=+v.h||0,a=+v.age||0;
      const bmr=v.gender==='m'?10*w+6.25*h-5*a+5:10*w+6.25*h-5*a-161;
      return [['BMR (Sedentary)',Math.round(bmr*1.2)+' cal/day'],['Moderate Active',Math.round(bmr*1.55)+' cal/day',true],['Very Active',Math.round(bmr*1.9)+' cal/day']];
    }
  },
  water: {
    name: 'Water Intake Calculator',
    fields: [
      {k:'w',l:'Weight (kg)',t:'number',v:70},
      {k:'activity',l:'Activity (min/day)',t:'number',v:30}
    ],
    calc: v => {
      const w=+v.w||0,a=+v.activity||0;
      const base=w*0.033;
      const extra=a/30*0.35;
      const total=base+extra;
      return [['Daily Water',total.toFixed(2)+' L',true],['Glasses (250ml)',Math.round(total*4)+' glasses']];
    }
  },
  pregnancy: {
    name: 'Pregnancy Due Date Calculator',
    fields: [{k:'lmp',l:'First Day of Last Period',t:'date',v:''}],
    calc: v => {
      if(!v.lmp)return [['Enter date','—']];
      const lmp=new Date(v.lmp);
      const due=new Date(lmp.getTime()+280*86400000);
      const today=new Date();
      const weeks=Math.floor((today-lmp)/86400000/7);
      return [['Due Date',due.toDateString(),true],['Currently',weeks+' weeks pregnant']];
    }
  },
  dateDiff: {
    name: 'Date Difference Calculator',
    fields: [
      {k:'from',l:'From Date',t:'date',v:''},
      {k:'to',l:'To Date',t:'date',v:''}
    ],
    calc: v => {
      if(!v.from||!v.to)return [['Enter both dates','—']];
      const d1=new Date(v.from),d2=new Date(v.to);
      const diff=Math.abs(d2-d1)/86400000;
      return [['Days',Math.round(diff),true],['Weeks',(diff/7).toFixed(1)],['Months',(diff/30.44).toFixed(1)]];
    }
  }
};

// ===== RENDER ENGINE =====
function renderCalc(elId, calcKey) {
  const calc = CALCS[calcKey];
  if (!calc) return;
  const el = document.getElementById(elId);
  if (!el) return;

  let html = `<h1 class="page-title">${calc.name}</h1>`;
  calc.fields.forEach(f => {
    html += `<div class="field"><label>${f.l}</label>`;
    if (f.t === 'select') {
      html += `<select data-k="${f.k}">`;
      f.o.forEach(([val, txt]) => { html += `<option value="${val}"${val == f.v ? ' selected' : ''}>${txt}</option>`; });
      html += `</select>`;
    } else if (f.t === 'radio') {
      html += `<div class="radio-group">`;
      f.o.forEach(([val, txt]) => { html += `<label><input type="radio" name="${calcKey}-${f.k}" value="${val}" data-k="${f.k}"${val == f.v ? ' checked' : ''}>${txt}</label>`; });
      html += `</div>`;
    } else {
      const minAttr = f.t === 'number' ? ' min="0"' : '';
      html += `<input type="${f.t}" data-k="${f.k}" value="${f.v}"${f.step ? ` step="${f.step}"` : ''}${minAttr}>`;
    }
    html += `</div>`;
  });
  html += `<div class="result show" data-result></div>`;
  el.innerHTML = html;

  const getValues = () => {
    const v = {};
    el.querySelectorAll('input,select').forEach(inp => {
      const k = inp.dataset.k;
      if (!k) return;
      if (inp.type === 'radio') { if (inp.checked) v[k] = inp.value; }
      else v[k] = inp.value;
    });
    return v;
  };

  const update = () => {
    const v = getValues();
    const resultDiv = el.querySelector('[data-result]');
    
    // Input validation: check for invalid numbers
    let hasError = false;
    calc.fields.forEach(f => {
      if (f.t === 'number') {
        const val = v[f.k];
        if (val === '' || val === undefined || isNaN(+val) || +val < 0) {
          hasError = true;
        }
      }
    });
    
    if (hasError) {
      resultDiv.innerHTML = '<div class="result-row"><span class="label">Please enter valid positive numbers</span></div>';
      return;
    }

    const out = calc.calc(v);
    resultDiv.innerHTML = out.map(([label, val, total]) =>
      `<div class="result-row${total ? ' total' : ''}"><span class="label">${label}</span><span class="value">${val}</span></div>`
    ).join('');
  };

  el.querySelectorAll('input,select').forEach(inp => {
    inp.addEventListener('input', update);
    inp.addEventListener('change', update);
  });
  update();
}

// Homepage: render all as tabs
function renderHome(containerId, tabsId) {
  const container = document.getElementById(containerId);
  const tabs = document.getElementById(tabsId);
  if (!container || !tabs) return;

  let first = true;
  Object.keys(CALCS).forEach(key => {
    const c = CALCS[key];
    const t = document.createElement('div');
    t.className = 'tab' + (first ? ' active' : '');
    t.textContent = c.name.replace(' Calculator', '');
    t.dataset.id = key;
    tabs.appendChild(t);

    const panel = document.createElement('div');
    panel.className = 'card calc-panel' + (first ? ' active' : '');
    panel.id = 'panel-' + key;
    container.appendChild(panel);

    renderCalc('panel-' + key, key);
    first = false;
  });

  tabs.querySelectorAll('.tab').forEach(t => {
    t.addEventListener('click', () => {
      tabs.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
      container.querySelectorAll('.calc-panel').forEach(x => x.classList.remove('active'));
      t.classList.add('active');
      document.getElementById('panel-' + t.dataset.id).classList.add('active');
    });
  });
}

// Render "Explore More Calculators" links (related only)
function renderRelatedLinks(currentCalcKey) {
  const container = document.getElementById('related-calculators');
  if (!container) return;

  let related = RELATED[currentCalcKey];
  if (!related) {
    related = Object.keys(CALCS).filter(k => k !== currentCalcKey).slice(0, 6);
  }

  let html = '<h2>Explore More Calculators</h2><div class="grid-cards">';
  related.forEach(key => {
    if (CALC_SLUGS[key] && CALCS[key]) {
      html += `<a href="/calculators/${CALC_SLUGS[key]}">${CALCS[key].name}</a>`;
    }
  });
  html += '</div>';
  container.innerHTML = html;
}