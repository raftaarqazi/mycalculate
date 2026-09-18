# add-faq-schemas.py
# Run from project root: python add-faq-schemas.py
# Safe to run multiple times — skips files that already have FAQPage

import os
import sys

# All 22 FAQ schema blocks
FAQS = {}

FAQS["calculators/age-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How is age calculated?","acceptedAnswer":{"@type":"Answer","text":"Age is calculated by subtracting date of birth from today, handling different month lengths and leap years. The formula borrows days from the previous month if needed, and months from the previous year if the birth month is later than current month."}},
{"@type":"Question","name":"Does this calculator account for leap years?","acceptedAnswer":{"@type":"Answer","text":"Yes. The calculator uses actual month lengths (28, 29, 30, or 31 days) when borrowing days, so leap years are automatically handled in the total days calculation."}},
{"@type":"Question","name":"Why is my age in years different from years-months-days?","acceptedAnswer":{"@type":"Answer","text":"The years-only number is your birthday-based age. Years-months-days gives the precise breakdown. For example, 25 years 8 months means you have completed 25 birthdays and 8 months toward the 26th."}},
{"@type":"Question","name":"How many days old am I?","acceptedAnswer":{"@type":"Answer","text":"Enter your date of birth and the calculator shows total days lived. For example, a person born on 1 January 2000 has lived approximately 9,400 days by September 2026."}},
{"@type":"Question","name":"Is this calculator accurate for government forms?","acceptedAnswer":{"@type":"Answer","text":"Yes. The calculator provides age in years, months, and days — the standard format required by most government forms, school admissions, and job applications in India."}},
{"@type":"Question","name":"Can I calculate age on a future date?","acceptedAnswer":{"@type":"Answer","text":"The current version uses today's date. For future-date age calculation, note your current age and add the difference manually, or use the Date Difference Calculator."}}
]}
</script>
'''

FAQS["calculators/bmi-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is BMI?","acceptedAnswer":{"@type":"Answer","text":"BMI (Body Mass Index) is a measure of body fat based on weight and height. It's calculated as weight in kg divided by height in meters squared. BMI is a screening tool, not a direct measure of body fat."}},
{"@type":"Question","name":"What is a healthy BMI range?","acceptedAnswer":{"@type":"Answer","text":"According to WHO, a healthy BMI is 18.5 to 24.9. Below 18.5 is underweight, 25 to 29.9 is overweight, and 30+ is obese. For Indians, some experts recommend slightly lower cutoffs (23 for overweight) due to higher body fat at lower BMI."}},
{"@type":"Question","name":"Is BMI accurate for athletes?","acceptedAnswer":{"@type":"Answer","text":"No. BMI doesn't distinguish between muscle and fat. Muscular athletes often show overweight or obese on BMI despite having low body fat. For athletes, use body fat percentage or waist circumference instead."}},
{"@type":"Question","name":"Is BMI the same for men and women?","acceptedAnswer":{"@type":"Answer","text":"The BMI formula and category cutoffs are the same for both. However, women naturally have more body fat than men at the same BMI. Interpretation should account for this difference, especially at borderline values."}},
{"@type":"Question","name":"What is BMI for children?","acceptedAnswer":{"@type":"Answer","text":"For children and teens, BMI is interpreted using age-and-gender-specific percentile charts, not the adult categories. Use our BMI Calculator for Kids page for accurate assessment."}},
{"@type":"Question","name":"Does BMI apply to pregnant women?","acceptedAnswer":{"@type":"Answer","text":"No. BMI is not accurate during pregnancy because of natural weight gain. Pregnant women should track weight gain against their pre-pregnancy BMI using charts recommended by their doctor."}}
]}
</script>
'''

FAQS["calculators/bmi-kids-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Is BMI calculated the same way for kids and adults?","acceptedAnswer":{"@type":"Answer","text":"The formula is the same (weight in kg divided by height in meters squared), but interpretation is completely different. Children's BMI is compared against age-and-gender-specific percentile charts, not adult categories."}},
{"@type":"Question","name":"What is a healthy BMI for a child?","acceptedAnswer":{"@type":"Answer","text":"Healthy weight is between the 5th and 85th percentile for the child's age and gender. Below 5th percentile is underweight, 85th-95th is overweight, and above 95th is obese. Only a pediatrician can interpret these percentiles properly."}},
{"@type":"Question","name":"Why do athletic kids show higher BMI?","acceptedAnswer":{"@type":"Answer","text":"BMI doesn't distinguish muscle from fat. Athletic children with high muscle mass may show elevated BMI despite low body fat. This is why BMI is a screening tool, not a diagnostic one."}},
{"@type":"Question","name":"When should I worry about my child's BMI?","acceptedAnswer":{"@type":"Answer","text":"Consult a pediatrician if BMI is below 5th percentile, above 85th percentile, or if there are sudden changes in weight, eating habits, or activity levels. Persistent concerns warrant professional review."}},
{"@type":"Question","name":"Does this calculator use CDC or WHO growth charts?","acceptedAnswer":{"@type":"Answer","text":"This calculator provides the raw BMI number only. To interpret against CDC or WHO growth charts, share the result with your pediatrician. Both chart systems have slightly different cutoffs."}},
{"@type":"Question","name":"How often should I check my child's BMI?","acceptedAnswer":{"@type":"Answer","text":"Once or twice a year during regular checkups is enough. Tracking monthly is unnecessary and may cause anxiety. Focus on overall healthy habits rather than the number on the scale."}}
]}
</script>
'''

FAQS["calculators/cagr-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is CAGR?","acceptedAnswer":{"@type":"Answer","text":"CAGR (Compound Annual Growth Rate) is the average annual growth rate of an investment over a period, assuming steady growth. It smooths out volatility to give one number that represents the investment's performance."}},
{"@type":"Question","name":"What is the CAGR formula?","acceptedAnswer":{"@type":"Answer","text":"CAGR = (Ending Value / Beginning Value)^(1/Years) - 1. The result is multiplied by 100 for percentage. This formula assumes steady compounding."}},
{"@type":"Question","name":"What is the difference between CAGR and absolute return?","acceptedAnswer":{"@type":"Answer","text":"Absolute return is total gain (e.g., 150%). CAGR is annualized (e.g., 20% per year). A 150% gain over 5 years equals 20% CAGR. CAGR is better for comparing investments of different durations."}},
{"@type":"Question","name":"Is CAGR suitable for SIP investments?","acceptedAnswer":{"@type":"Answer","text":"No. CAGR assumes a lump sum invested once. For SIPs with multiple instalments, use XIRR (Extended Internal Rate of Return), which handles irregular cash flows accurately."}},
{"@type":"Question","name":"Why is CAGR important for mutual funds?","acceptedAnswer":{"@type":"Answer","text":"CAGR lets you compare mutual funds across different time periods on equal footing. A fund delivering 12% CAGR over 10 years can be compared fairly with one delivering 15% over 5 years."}},
{"@type":"Question","name":"Does CAGR include dividends or taxes?","acceptedAnswer":{"@type":"Answer","text":"Standard CAGR does not include dividends unless reinvested, and does not account for taxes. For post-tax comparison, subtract the tax rate from the final value before calculating CAGR."}}
]}
</script>
'''

FAQS["calculators/calorie-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is BMR and TDEE?","acceptedAnswer":{"@type":"Answer","text":"BMR (Basal Metabolic Rate) is calories your body burns at rest. TDEE (Total Daily Energy Expenditure) is BMR multiplied by an activity factor, representing total daily calorie burn including exercise and daily movement."}},
{"@type":"Question","name":"Which formula is most accurate for BMR?","acceptedAnswer":{"@type":"Answer","text":"The Mifflin-St Jeor formula is considered the most accurate for most people. It uses weight, height, age, and gender. The Harris-Benedict formula is older but slightly less accurate."}},
{"@type":"Question","name":"How many calories should I eat to lose weight?","acceptedAnswer":{"@type":"Answer","text":"A deficit of 500 calories per day from your TDEE leads to roughly 0.5 kg weight loss per week. Eating below 1,200 calories (women) or 1,500 calories (men) is generally not recommended without medical supervision."}},
{"@type":"Question","name":"Do I need to eat back the calories I burn during exercise?","acceptedAnswer":{"@type":"Answer","text":"No. TDEE already includes your typical activity. Only add extra calories if you did unusually intense or long workouts. Otherwise, count the total TDEE as your daily target."}},
{"@type":"Question","name":"How accurate is a calorie calculator?","acceptedAnswer":{"@type":"Answer","text":"The calculator gives an estimate based on average formulas. Individual metabolism varies by 10-15%. Use it as a starting point, then adjust based on real-world results over 2-3 weeks."}},
{"@type":"Question","name":"Do calories from protein, carbs, and fat matter equally?","acceptedAnswer":{"@type":"Answer","text":"No. Protein and carbs provide 4 calories per gram, fat provides 9 calories per gram. For weight loss, total calorie intake matters most, but protein helps preserve muscle, and fiber helps with satiety."}}
]}
</script>
'''

FAQS["calculators/car-loan-emi-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is the current car loan interest rate in India?","acceptedAnswer":{"@type":"Answer","text":"As of 2026, car loan rates range from 8.5% to 14% depending on the bank, your credit score, and whether it's a new or used car. New cars get lower rates than used cars."}},
{"@type":"Question","name":"What is the maximum tenure for a car loan?","acceptedAnswer":{"@type":"Answer","text":"Most banks offer car loans up to 7 years (84 months). Some NBFCs offer up to 8 years. Longer tenures mean lower EMI but higher total interest paid."}},
{"@type":"Question","name":"Should I make a bigger down payment?","acceptedAnswer":{"@type":"Answer","text":"Yes, if possible. A 20-30% down payment reduces the loan amount, lowers EMI, reduces total interest, and improves loan approval chances. It also protects against depreciation."}},
{"@type":"Question","name":"Can I prepay my car loan?","acceptedAnswer":{"@type":"Answer","text":"Most banks allow prepayment after 6-12 EMI payments. Some charge a 2-4% foreclosure fee on floating-rate loans. Check the terms before taking the loan."}},
{"@type":"Question","name":"Does car loan interest qualify for tax deduction?","acceptedAnswer":{"@type":"Answer","text":"Only if the car is used for business purposes. Personal car loan interest is not tax-deductible. For business vehicles, interest can be claimed as a business expense."}},
{"@type":"Question","name":"Is it better to buy a new or used car on loan?","acceptedAnswer":{"@type":"Answer","text":"New cars get lower interest rates (8.5-11%) and longer tenure but depreciate faster. Used cars have higher rates (12-16%) and shorter tenure but lower absolute price. Choose based on your budget and how long you'll keep the car."}}
]}
</script>
'''

FAQS["calculators/compound-interest-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is compound interest?","acceptedAnswer":{"@type":"Answer","text":"Compound interest is interest calculated on both the principal and accumulated interest. Over time, this creates exponential growth because interest earns its own interest. It's the basis of most investment returns."}},
{"@type":"Question","name":"What is the compound interest formula?","acceptedAnswer":{"@type":"Answer","text":"A = P x (1 + R/N)^(N x T), where P is principal, R is annual rate as decimal, N is compounding frequency per year, and T is time in years. Compound interest = A - P."}},
{"@type":"Question","name":"How does compounding frequency affect returns?","acceptedAnswer":{"@type":"Answer","text":"More frequent compounding = higher returns. Monthly compounding gives slightly more than quarterly, which gives more than annual. On 10,000 at 7.5% for 3 years: annual gives 12,423, monthly gives 12,491."}},
{"@type":"Question","name":"What is the difference between simple and compound interest?","acceptedAnswer":{"@type":"Answer","text":"Simple interest is calculated only on principal, growing linearly. Compound interest is calculated on principal plus accumulated interest, growing exponentially. Over long periods, compound interest gives much higher returns."}},
{"@type":"Question","name":"Does compound interest work against me on loans?","acceptedAnswer":{"@type":"Answer","text":"Yes. Credit card debt compounds daily at 36-42% annual rate, making balances grow very fast. Any loan with compound interest becomes expensive if not repaid quickly. Pay off high-interest debt aggressively."}},
{"@type":"Question","name":"What is the Rule of 72?","acceptedAnswer":{"@type":"Answer","text":"The Rule of 72 estimates how long an investment takes to double: 72 divided by interest rate = years to double. At 12% return, money doubles in approximately 6 years. At 8%, it doubles in 9 years."}}
]}
</script>
'''

FAQS["calculators/currency-converter.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How often are exchange rates updated?","acceptedAnswer":{"@type":"Answer","text":"This calculator uses approximate static rates updated periodically. For live rates, check RBI reference rates, XE.com, or your bank's forex desk. Rates fluctuate throughout the trading day."}},
{"@type":"Question","name":"Why do banks give a different rate than Google?","acceptedAnswer":{"@type":"Answer","text":"Banks add a markup of 1-3% above the interbank rate to cover risk and profit. Google shows the interbank rate. For actual transactions, you'll get the bank's rate, not Google's."}},
{"@type":"Question","name":"What is the best time to exchange currency?","acceptedAnswer":{"@type":"Answer","text":"Rates fluctuate minute to minute. For large amounts, monitor rates for a few days and exchange during favourable movement. Avoid airport kiosks — they charge the highest markups."}},
{"@type":"Question","name":"Are there limits on how much foreign currency I can carry?","acceptedAnswer":{"@type":"Answer","text":"For Indian residents travelling abroad: up to USD 3,000 in cash per trip. For NRIs visiting India: up to USD 5,000 in cash. Amounts above this must be declared. Check current RBI guidelines before travel."}},
{"@type":"Question","name":"Which currency is strongest in the world?","acceptedAnswer":{"@type":"Answer","text":"By nominal value against INR, the Kuwaiti Dinar (KWD) is strongest, followed by Bahraini Dinar (BHD) and Omani Rial (OMR). The US Dollar is the most traded globally but not the highest-valued."}},
{"@type":"Question","name":"Why does the rupee value change against the dollar?","acceptedAnswer":{"@type":"Answer","text":"Rupee-dollar rate changes based on inflation differential, interest rate differential, oil prices, foreign investment flows, and RBI intervention. Higher US interest rates typically strengthen the dollar against the rupee."}}
]}
</script>
'''

FAQS["calculators/date-difference-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How is date difference calculated?","acceptedAnswer":{"@type":"Answer","text":"Both dates are converted to milliseconds since the Unix epoch, the difference is taken, and the result is divided by 86,400,000 (milliseconds in a day) to get the number of days. Weeks = days/7, months = days/30.44."}},
{"@type":"Question","name":"Are leap years considered?","acceptedAnswer":{"@type":"Answer","text":"Yes. Since the calculation uses actual calendar dates and milliseconds, leap years are automatically factored in. A difference spanning February 29 will count the extra day correctly."}},
{"@type":"Question","name":"Is the end date included in the count?","acceptedAnswer":{"@type":"Answer","text":"The calculator shows the absolute difference between two dates. If you want to include both start and end dates, add 1 to the day count. This matters for events like hotel stays."}},
{"@type":"Question","name":"What is the difference between working days and calendar days?","acceptedAnswer":{"@type":"Answer","text":"Calendar days count every day including weekends and holidays. Working days exclude Saturdays, Sundays, and public holidays. This calculator shows calendar days."}},
{"@type":"Question","name":"Can I calculate age using this?","acceptedAnswer":{"@type":"Answer","text":"You can calculate total days lived, but for exact age in years-months-days format, use the Age Calculator. That handles month-length and leap-year borrowing for a proper breakdown."}},
{"@type":"Question","name":"How is the month count calculated?","acceptedAnswer":{"@type":"Answer","text":"Months are calculated by dividing total days by 30.44 (average month length over a 4-year cycle). This is approximate since actual months vary from 28 to 31 days."}}
]}
</script>
'''

FAQS["calculators/discount-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How is discount calculated?","acceptedAnswer":{"@type":"Answer","text":"Discount amount = Original Price x Discount % / 100. Final price = Original Price minus Discount amount. For 1,000 at 20% off, discount is 200, final price is 800."}},
{"@type":"Question","name":"What is a stacked discount?","acceptedAnswer":{"@type":"Answer","text":"Stacked discount means applying one discount on top of another. A 20% off plus extra 10% off is NOT 30% off — it's 28% off. The second discount applies to the already-reduced price, not the original."}},
{"@type":"Question","name":"Is 20% off the same as pay for 4 get 5?","acceptedAnswer":{"@type":"Answer","text":"No. 20% off means you pay 80% of the price. Pay for 4 get 5 means 5 items for the price of 4, which is 20% off per item. They're equivalent in total."}},
{"@type":"Question","name":"How do I check if a discount is genuine?","acceptedAnswer":{"@type":"Answer","text":"Compare final price with the product's price at other stores, not with the MRP. Some sellers inflate the MRP to show a larger discount. The actual final price is what matters."}},
{"@type":"Question","name":"What does up to X percent off mean?","acceptedAnswer":{"@type":"Answer","text":"Up to 50% off means some items are at 50% but most are at lower discounts. It's a marketing tactic. Always check the specific item's discount, not the banner."}},
{"@type":"Question","name":"Does GST apply before or after discount?","acceptedAnswer":{"@type":"Answer","text":"GST is calculated on the discounted price, not on the original MRP. If a 1,000 item is 20% off, GST applies to the 800 final price, not 1,000."}}
]}
</script>
'''

FAQS["calculators/fd-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How is FD interest calculated?","acceptedAnswer":{"@type":"Answer","text":"Most banks use compound interest for FDs: Maturity = P x (1 + R/100)^T. Some banks use quarterly compounding. The compounding frequency slightly changes the final amount."}},
{"@type":"Question","name":"Is FD interest taxable?","acceptedAnswer":{"@type":"Answer","text":"Yes. FD interest is added to your total income and taxed at your slab rate. If interest exceeds 40,000 per bank per year (50,000 for senior citizens), the bank deducts 10% TDS. Post-tax return at 30% slab on a 7% FD is roughly 5%."}},
{"@type":"Question","name":"What is the difference between cumulative and non-cumulative FD?","acceptedAnswer":{"@type":"Answer","text":"Cumulative FD reinvests interest — you get a lump sum at maturity with compounded returns. Non-cumulative FD pays interest monthly or quarterly — useful for regular income but no compounding."}},
{"@type":"Question","name":"Is FD safe?","acceptedAnswer":{"@type":"Answer","text":"Yes, FDs are among the safest instruments. DICGC insures deposits up to 5 lakh per bank per depositor. For larger amounts, split across multiple banks to stay within the insurance limit."}},
{"@type":"Question","name":"What happens if I break my FD early?","acceptedAnswer":{"@type":"Answer","text":"Breaking an FD before maturity usually incurs a penalty of 0.5-1% on the applicable interest rate. Some banks waive the penalty for genuine emergencies. Use loan against FD instead of breaking it."}},
{"@type":"Question","name":"FD vs PPF — which is better?","acceptedAnswer":{"@type":"Answer","text":"FD has 1-5 year lock-in and taxable returns (7-7.5% pre-tax). PPF has 15-year lock-in and fully tax-free returns (7.1% currently). For short-term goals, FD. For long-term retirement, PPF."}}
]}
</script>
'''

FAQS["calculators/gratuity-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is the gratuity formula?","acceptedAnswer":{"@type":"Answer","text":"Gratuity = (15 x Last Drawn Salary x Years of Service) / 26. Last Drawn Salary means Basic + Dearness Allowance. Years of service over 6 months in a year are rounded up to the next full year."}},
{"@type":"Question","name":"Who is eligible for gratuity?","acceptedAnswer":{"@type":"Answer","text":"Employees who have completed 5 years of continuous service with an employer covered under the Payment of Gratuity Act, 1972. The 5-year rule is waived in case of death or disability."}},
{"@type":"Question","name":"Is gratuity taxable?","acceptedAnswer":{"@type":"Answer","text":"Gratuity up to 20 lakh is exempt from tax for private sector employees. Government employees have no cap. Amounts above 20 lakh are taxed as per income slab."}},
{"@type":"Question","name":"When must gratuity be paid?","acceptedAnswer":{"@type":"Answer","text":"The employer must pay gratuity within 30 days from the date it becomes due. If delayed, the employer pays simple interest on the amount. You can file a complaint with the labour commissioner if not paid."}},
{"@type":"Question","name":"Is gratuity paid if I resign?","acceptedAnswer":{"@type":"Answer","text":"Yes, if you've completed 5 years of continuous service. Gratuity applies on retirement, resignation, superannuation, or termination (except for misconduct). It's not a benefit only for retirees."}},
{"@type":"Question","name":"How is partial year of service counted?","acceptedAnswer":{"@type":"Answer","text":"Service of more than 6 months in the final year counts as 1 full year. Service of 6 months or less is ignored. For example, 4 years 8 months = 5 years for gratuity calculation."}}
]}
</script>
'''

FAQS["calculators/hra-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How is HRA exemption calculated?","acceptedAnswer":{"@type":"Answer","text":"HRA exemption is the minimum of three values: (1) Actual HRA received, (2) 50% of basic salary for metro cities or 40% for non-metro, (3) Rent paid minus 10% of basic salary. The lowest amount is tax-exempt."}},
{"@type":"Question","name":"Which cities are considered metro for HRA?","acceptedAnswer":{"@type":"Answer","text":"Only Delhi, Mumbai, Kolkata, and Chennai are metro cities for HRA purposes. Bangalore, Hyderabad, and Pune are non-metro despite being large cities. Metro gets the 50% rule, non-metro gets 40%."}},
{"@type":"Question","name":"Can I claim HRA if I live in my own house?","acceptedAnswer":{"@type":"Answer","text":"No. HRA exemption requires actually paying rent. If you live in your own house, there's no rent. But you can claim home loan interest deduction under Section 24 (up to 2 lakh) for a self-occupied property."}},
{"@type":"Question","name":"What documents are needed for HRA claim?","acceptedAnswer":{"@type":"Answer","text":"Rent receipts, rent agreement, and if rent exceeds 1 lakh per year, the landlord's PAN. Submit these to your employer via Form 12BB at the start of the financial year to avoid higher TDS."}},
{"@type":"Question","name":"Can I claim HRA and home loan interest together?","acceptedAnswer":{"@type":"Answer","text":"Yes, under specific conditions: you must live in a rented house while owning a property in another city (rented out). This is common when you work away from your hometown. Consult a CA for the exact conditions."}},
{"@type":"Question","name":"Can I pay rent to my parents and claim HRA?","acceptedAnswer":{"@type":"Answer","text":"Yes, if they own the property, you actually pay rent via bank transfer, and they declare it as rental income in their ITR. Paying rent to a spouse is heavily scrutinized and generally not recommended."}}
]}
</script>
'''

FAQS["calculators/income-tax-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Which tax regime is better — old or new?","acceptedAnswer":{"@type":"Answer","text":"No universal answer. If your total deductions (80C, 80D, HRA, home loan interest) exceed 3-4 lakh, the old regime usually wins. If deductions are minimal (under 1.5 lakh), the new regime is typically better. Run the calculator with your specific numbers."}},
{"@type":"Question","name":"What are the new regime tax slabs for FY 2025-26?","acceptedAnswer":{"@type":"Answer","text":"New Regime slabs: 0-3L nil, 3-6L 5%, 6-9L 10%, 9-12L 15%, 12-15L 20%, above 15L 30%. Standard deduction of 50,000 applies to both regimes."}},
{"@type":"Question","name":"Can I switch tax regimes every year?","acceptedAnswer":{"@type":"Answer","text":"Salaried employees can switch between old and new regimes every year at the time of filing ITR. Business owners with business income can only switch once in their lifetime."}},
{"@type":"Question","name":"Is the new tax regime mandatory?","acceptedAnswer":{"@type":"Answer","text":"The new regime is the default for taxpayers without business income. You can opt for the old regime at the time of filing ITR if it's more beneficial. Communicate your choice to HR at the start of the financial year."}},
{"@type":"Question","name":"What is standard deduction?","acceptedAnswer":{"@type":"Answer","text":"Standard deduction of 50,000 is a flat deduction available to salaried taxpayers in both regimes. It's deducted from gross salary before applying slabs. No receipts or investments required."}},
{"@type":"Question","name":"How is tax calculated on 20 lakh income?","acceptedAnswer":{"@type":"Answer","text":"On the new regime, tax on 20 lakh is roughly 3 lakh (including cess). On the old regime with substantial deductions, it can be lower. Use this calculator with your exact numbers to compare both regimes."}}
]}
</script>
'''

FAQS["calculators/loan-eligibility-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How is loan eligibility calculated?","acceptedAnswer":{"@type":"Answer","text":"Banks use FOIR (Fixed Obligation to Income Ratio). Maximum EMI allowed is typically 50% of monthly income. Existing EMIs are subtracted. The remaining amount is available for the new EMI, from which loan amount is calculated based on tenure and rate."}},
{"@type":"Question","name":"What is FOIR?","acceptedAnswer":{"@type":"Answer","text":"FOIR (Fixed Obligation to Income Ratio) is the ratio of total EMIs to monthly income. Banks prefer a FOIR below 50%. A lower FOIR improves eligibility and gets better interest rates."}},
{"@type":"Question","name":"Does a longer tenure increase eligibility?","acceptedAnswer":{"@type":"Answer","text":"Yes. Longer tenure means lower EMI, so you can borrow more with the same monthly income. But longer tenure also means higher total interest paid. Balance eligibility against total cost."}},
{"@type":"Question","name":"How does credit score affect loan eligibility?","acceptedAnswer":{"@type":"Answer","text":"A credit score of 750+ gets you the best rates and highest eligibility. Scores below 650 may result in rejection or much higher rates. Improve your score before applying to expand options."}},
{"@type":"Question","name":"Can I add a co-applicant to increase eligibility?","acceptedAnswer":{"@type":"Answer","text":"Yes. Adding a spouse, parent, or sibling with income adds their income to the pool and can increase eligibility by 50-100%. Both applicants become jointly liable for repayment."}},
{"@type":"Question","name":"What documents are required for loan approval?","acceptedAnswer":{"@type":"Answer","text":"Standard documents include identity proof (Aadhaar, PAN), address proof, salary slips (last 3-6 months), bank statements (6 months), Form 16, and ITR (2-3 years). Property documents are required for home loans."}}
]}
</script>
'''

FAQS["calculators/lumpsum-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is lumpsum investment?","acceptedAnswer":{"@type":"Answer","text":"Lumpsum investment is investing a large amount at once in a mutual fund, as opposed to SIP. It's suitable when you have a surplus (bonus, inheritance, property sale) and a long investment horizon (7+ years)."}},
{"@type":"Question","name":"Is lumpsum better than SIP?","acceptedAnswer":{"@type":"Answer","text":"In a rising market, lumpsum wins because your full amount compounds from day one. In a volatile market, SIP wins because rupee-cost averaging reduces timing risk. For most retail investors without market timing skill, SIP is safer."}},
{"@type":"Question","name":"What is the lumpsum formula?","acceptedAnswer":{"@type":"Answer","text":"Future Value = P x (1 + R)^N, where P is investment amount, R is annual return rate (as decimal), and N is years. 1 lakh at 12% for 10 years becomes 3.1 lakh."}},
{"@type":"Question","name":"When should I avoid lumpsum?","acceptedAnswer":{"@type":"Answer","text":"Avoid lumpsum if markets are at all-time highs, if you need the money within 2-3 years, if you're a beginner investor, or if you can't handle short-term volatility. In these cases, stagger the investment over 6-12 months via STP."}},
{"@type":"Question","name":"What is STP and how is it different from lumpsum?","acceptedAnswer":{"@type":"Answer","text":"STP (Systematic Transfer Plan) means investing lumpsum in a debt fund and transferring it to equity gradually. It combines lumpsum availability with SIP-like averaging. Good middle ground for large windfalls."}},
{"@type":"Question","name":"How is lumpsum taxed?","acceptedAnswer":{"@type":"Answer","text":"Equity mutual fund LTCG (holding over 1 year) above 1.25 lakh per year is taxed at 12.5%. Short-term gains (under 1 year) are taxed at 20%. Debt funds are taxed as per your income slab."}}
]}
</script>
'''

FAQS["calculators/personal-loan-emi-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is a personal loan?","acceptedAnswer":{"@type":"Answer","text":"A personal loan is an unsecured loan — no collateral required. Banks offer it based on income and credit score. Interest rates (10.5-24%) are higher than secured loans because there's no asset backing."}},
{"@type":"Question","name":"What is the maximum personal loan amount?","acceptedAnswer":{"@type":"Answer","text":"Most banks offer personal loans from 50,000 up to 50 lakh, depending on your income, credit score, and existing obligations. Pre-approved offers can go higher for existing customers."}},
{"@type":"Question","name":"How long does personal loan approval take?","acceptedAnswer":{"@type":"Answer","text":"Approval typically takes 24-72 hours. Disbursement is same-day or next-day after approval. Pre-approved customers often get same-day disbursement if documents are ready."}},
{"@type":"Question","name":"What is the processing fee on a personal loan?","acceptedAnswer":{"@type":"Answer","text":"Processing fee is usually 1-3% of the loan amount. On a 5 lakh loan, that's 5,000-15,000, deducted at disbursement. Some banks charge 0% processing fee as a promotional offer."}},
{"@type":"Question","name":"Can I prepay a personal loan?","acceptedAnswer":{"@type":"Answer","text":"Most banks allow prepayment after 6-12 EMIs. Prepayment charges range from 0% to 4% of the outstanding amount. Some banks offer zero prepayment penalty as a feature. Check the terms before signing."}},
{"@type":"Question","name":"When should I avoid a personal loan?","acceptedAnswer":{"@type":"Answer","text":"Avoid personal loans for luxury purchases, gadgets, vacations, or investing in stocks/mutual funds. Personal loan rates (10.5-24%) are much higher than expected market returns. Use personal loans only for genuine needs: medical emergencies, weddings, education, or debt consolidation."}}
]}
</script>
'''

FAQS["calculators/pregnancy-due-date-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How is pregnancy due date calculated?","acceptedAnswer":{"@type":"Answer","text":"Using Naegele's Rule: first day of last menstrual period (LMP) + 280 days (40 weeks). This assumes a regular 28-day cycle. For irregular cycles, an early ultrasound gives a more accurate due date."}},
{"@type":"Question","name":"How accurate is the due date?","acceptedAnswer":{"@type":"Answer","text":"Only about 5% of babies are born on their exact due date. Most births occur between weeks 38-42. An early ultrasound (before week 12) is the most accurate method to determine due date."}},
{"@type":"Question","name":"What is the difference between gestational age and fetal age?","acceptedAnswer":{"@type":"Answer","text":"Gestational age is counted from LMP and includes the 2 weeks before conception. Fetal age is counted from conception. Gestational age is typically 2 weeks more than fetal age and is the standard used by doctors."}},
{"@type":"Question","name":"What are the three trimesters?","acceptedAnswer":{"@type":"Answer","text":"First trimester: weeks 1-12 (organ development, morning sickness). Second trimester: weeks 13-27 (baby grows, movements felt). Third trimester: weeks 28-40 (final growth, preparation for birth)."}},
{"@type":"Question","name":"Does a longer cycle mean a later due date?","acceptedAnswer":{"@type":"Answer","text":"Yes. If your cycle is longer than 28 days, you likely ovulate later, so the due date shifts later. A 35-day cycle shifts the due date by about 7 days. An early ultrasound adjusts for this automatically."}},
{"@type":"Question","name":"When should I see a doctor after a positive pregnancy test?","acceptedAnswer":{"@type":"Answer","text":"Schedule your first prenatal appointment within 6-8 weeks of your LMP. Early prenatal care helps monitor development, screen for complications, and establish an accurate due date via ultrasound."}}
]}
</script>
'''

FAQS["calculators/salary-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is the difference between CTC and take-home salary?","acceptedAnswer":{"@type":"Answer","text":"CTC (Cost to Company) includes employer PF, gratuity, and insurance. Take-home is what reaches your bank after employee PF, income tax, and professional tax. On 8 LPA CTC, take-home is roughly 58,000-62,000 per month."}},
{"@type":"Question","name":"Why is my take-home so much lower than CTC/12?","acceptedAnswer":{"@type":"Answer","text":"Three things come out before you see money: employer PF (12% of basic), gratuity (4.81% of basic), and insurance premiums. Then employee PF and income tax further reduce take-home. Expect 20-25% less than CTC/12."}},
{"@type":"Question","name":"Is PF deduction mandatory?","acceptedAnswer":{"@type":"Answer","text":"Yes, for employees in establishments with 20+ employees. Contribution is 12% of basic (up to 15,000 basic). You can opt for VPF (Voluntary PF) to contribute more. PF earns 8.25% tax-free interest."}},
{"@type":"Question","name":"What is professional tax?","acceptedAnswer":{"@type":"Answer","text":"Professional tax is a state-level tax on income, deducted from salary. Rates vary by state — 200-2,500 per year. Maharashtra, Karnataka, and West Bengal charge it; Delhi doesn't."}},
{"@type":"Question","name":"How can I increase my take-home salary?","acceptedAnswer":{"@type":"Answer","text":"Three strategies: (1) Claim HRA exemption with rent receipts. (2) Structure salary with Flexible Benefit Plans (meal cards, LTA, fuel). (3) Choose the tax regime that fits your deductions. Can increase take-home by 20,000-50,000 per year."}},
{"@type":"Question","name":"What is the standard deduction in the new tax regime?","acceptedAnswer":{"@type":"Answer","text":"50,000 per year, same as the old regime. It's a flat deduction from gross salary, no receipts required. On 10 LPA, only 9.5L is taxable after standard deduction."}}
]}
</script>
'''

FAQS["calculators/simple-interest-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is simple interest?","acceptedAnswer":{"@type":"Answer","text":"Simple interest is calculated only on the original principal, not on accumulated interest. It grows linearly. Formula: SI = (P x R x T) / 100, where P is principal, R is annual rate, T is time in years."}},
{"@type":"Question","name":"What is the difference between simple and compound interest?","acceptedAnswer":{"@type":"Answer","text":"Simple interest grows linearly (same interest each year). Compound interest grows exponentially (interest earns interest). Over long periods, compound interest gives much higher returns. Banks offer compound on deposits and reducing-balance EMIs on loans."}},
{"@type":"Question","name":"Where is simple interest used?","acceptedAnswer":{"@type":"Answer","text":"Simple interest is used in short-term loans, informal lending, some NBFC flat-rate loans, bonds with coupon payments, and educational contexts. Most bank products use compound interest."}},
{"@type":"Question","name":"Is simple interest always better than compound interest?","acceptedAnswer":{"@type":"Answer","text":"For borrowers, yes — simple interest means paying less total interest. For investors, no — compound interest grows wealth faster. The choice depends on whether you're borrowing or investing."}},
{"@type":"Question","name":"What is the difference between simple interest and flat rate?","acceptedAnswer":{"@type":"Answer","text":"Flat rate loans use simple interest on the full principal for the full tenure, then collect it via monthly EMIs. A 10% flat rate is roughly equal to 18% reducing balance. Always compare loans on reducing-balance terms."}},
{"@type":"Question","name":"How do I calculate simple interest manually?","acceptedAnswer":{"@type":"Answer","text":"Multiply principal x rate x time, then divide by 100. For 50,000 at 10% for 2 years: (50,000 x 10 x 2) / 100 = 10,000 interest. Total amount = 60,000."}}
]}
</script>
'''

FAQS["calculators/temperature-converter.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How do I convert Celsius to Fahrenheit?","acceptedAnswer":{"@type":"Answer","text":"Formula: F = (C x 9/5) + 32. For example, 25C = (25 x 1.8) + 32 = 77F. Multiply first, then add the offset."}},
{"@type":"Question","name":"How do I convert Fahrenheit to Celsius?","acceptedAnswer":{"@type":"Answer","text":"Formula: C = (F - 32) x 5/9. For example, 98.6F = (98.6 - 32) x 5/9 = 37C. Subtract the offset first, then multiply."}},
{"@type":"Question","name":"What is Kelvin and when is it used?","acceptedAnswer":{"@type":"Answer","text":"Kelvin (K) is the scientific temperature scale starting at absolute zero (0K = -273.15C). Used in physics, chemistry, and engineering where ratios matter. No negative values — 0K is the coldest possible temperature."}},
{"@type":"Question","name":"Why is Fahrenheit used in the US?","acceptedAnswer":{"@type":"Answer","text":"The Fahrenheit scale was developed in 1724 and was widely adopted before Celsius became standard. The US, Bahamas, and Cayman Islands still use it for everyday weather and cooking. Scientific contexts use Celsius or Kelvin."}},
{"@type":"Question","name":"At what temperature are Celsius and Fahrenheit equal?","acceptedAnswer":{"@type":"Answer","text":"At -40 degrees, C = F. This is the only value where the two scales show the same number. Below -40, Celsius is higher numerically; above -40, Fahrenheit is higher."}},
{"@type":"Question","name":"What is normal body temperature?","acceptedAnswer":{"@type":"Answer","text":"37C or 98.6F is considered normal. But normal varies by person and time of day — 36.1-37.2C (97-99F) is a healthy range. Fever is generally above 38C (100.4F)."}}
]}
</script>
'''

FAQS["calculators/tip-calculator.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How much tip should I leave?","acceptedAnswer":{"@type":"Answer","text":"In India, tipping is optional. 5-10% for average service, 10-15% for good service, 15-20% for excellent. For small bills (chai, snacks, delivery), 20-50 is standard. In the US, 15-20% is expected because servers depend on tips."}},
{"@type":"Question","name":"Is service charge the same as tip?","acceptedAnswer":{"@type":"Answer","text":"No. Service charge (usually 5-10%) is added to the bill by the restaurant and shared among staff. Tipping is separate and given directly to the server. If service charge is already added, you don't need to tip extra."}},
{"@type":"Question","name":"Should I tip on the pre-tax or post-tax amount?","acceptedAnswer":{"@type":"Answer","text":"Tip is usually calculated on the pre-tax bill amount. Some people tip on the total. Either is acceptable — tipping on the pre-tax amount is the standard recommendation."}},
{"@type":"Question","name":"How do I split a bill among friends?","acceptedAnswer":{"@type":"Answer","text":"Enter the total bill, tip percentage, and number of people. The calculator divides the total equally. For unequal splits (someone ordered more), calculate each person's share separately."}},
{"@type":"Question","name":"Do I need to tip for delivery orders?","acceptedAnswer":{"@type":"Answer","text":"Yes, delivery apps pay riders per order, so tips matter. 20-50 is standard depending on order size and distance. Cash tips are often preferred over in-app tips because they're received faster."}},
{"@type":"Question","name":"Is tipping customary in India?","acceptedAnswer":{"@type":"Answer","text":"Tipping is optional but appreciated. Unlike the US, Indian servers are paid regular wages and don't depend on tips. Common scenarios: restaurants (5-10%), delivery (20-50), salon/spa (50-200), hotel staff (50-100 per service)."}}
]}
</script>
'''

FAQS["calculators/unit-converter.html"] = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"How do I convert km to miles?","acceptedAnswer":{"@type":"Answer","text":"Multiply km by 0.621371. For example, 10 km = 6.21371 miles. Reverse: multiply miles by 1.60934 to get km. For rough estimate, remember 1 km is about 0.6 miles."}},
{"@type":"Question","name":"How do I convert kg to pounds?","acceptedAnswer":{"@type":"Answer","text":"Multiply kg by 2.20462. For example, 70 kg = 154.32 pounds. Reverse: multiply pounds by 0.453592 to get kg. For rough estimate, 1 kg is about 2.2 pounds."}},
{"@type":"Question","name":"What is the difference between metric and imperial?","acceptedAnswer":{"@type":"Answer","text":"Metric (SI) uses base-10 multiples — km, m, cm, kg, g. Used by almost all countries. Imperial uses non-decimal units — mile, yard, foot, pound, ounce. Used in the US, UK, and a few others."}},
{"@type":"Question","name":"Why does the US use imperial units?","acceptedAnswer":{"@type":"Answer","text":"Historical reasons. The US adopted British imperial units before metric standardisation spread globally. Today the US is the only major country that primarily uses imperial for everyday measurements."}},
{"@type":"Question","name":"How do I convert feet to meters?","acceptedAnswer":{"@type":"Answer","text":"Multiply feet by 0.3048. For example, 10 feet = 3.048 meters. Reverse: multiply meters by 3.28084 to get feet. A person 5 feet 6 inches tall is 1.676 meters."}},
{"@type":"Question","name":"What is the most accurate way to convert units?","acceptedAnswer":{"@type":"Answer","text":"Use exact conversion factors (like 1 inch = 2.54 cm exactly, by definition). For everyday use, rounded values like 1 kg = 2.2 pounds work fine. For scientific or engineering use, always use the precise factor."}}
]}
</script>
'''


def add_faq(file_path, faq_block):
    if not os.path.isfile(file_path):
        print(f"  SKIP: {file_path} not found")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '"FAQPage"' in content:
        print(f"  SKIP: {file_path} already has FAQPage")
        return

    marker = '<link rel="stylesheet" href="/style.css">'
    if marker not in content:
        print(f"  WARN: marker not found in {file_path}")
        return

    content = content.replace(marker, faq_block + marker, 1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  DONE: {file_path}")


def main():
    print("")
    print("=" * 50)
    print("  Adding FAQPage schemas to calculators")
    print("=" * 50)
    print("")

    count = 0
    for file_path, faq_block in FAQS.items():
        add_faq(file_path, faq_block)
        count += 1

    print("")
    print("=" * 50)
    print(f"  Processed {count} files")
    print("=" * 50)
    print("")
    print("Next steps:")
    print("  1. Open one file, search for 'FAQPage' to verify")
    print("  2. git add .")
    print("  3. git commit -m 'Add FAQPage schemas to calculators'")
    print("  4. git push origin main")
    print("")


if __name__ == "__main__":
    main()