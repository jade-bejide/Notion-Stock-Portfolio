# Notion-Stock-Portfolio
Uses python and a bash script to automate the updation of your stock portfolio to the relevant Notion subpage.

## Sources
This code builds on work made by the creatir 'Coding and Fun' and a link to the original work can be viewed at: <a href="https://codingandfun.com/creating-a-portfolio-tracker-in-notion-with-python/">Coding and Fun</a>. 

What's different about this python script is that I store the tickers as a dictionary of dictionaries, for speed of access as well as to store more detail about the stock such as the buy price and number of holdings. I have also automated the python script to run every Friday using a batch file and Windows Task Scheduler and details of that can be found at: 
<a href="https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279">Towards Data Science</a>

For this to work, you'll need to set up a Notion page and create an inline table with the following headings:

<ol>
  <li>Date</li>
  <li>Stock</li>
  <li>Original_Price</li>
  <li>Current_Price</li>
  <li>NumOfStock</li>
  <li>Amount</li>
  <li>Profit</li>
 </ol>
