# Django Rest Framework Project

In this project user can create wallets and conduct transactions between them. 
When creating a new wallet, a bonus is added to the user's balance. 
The user cannot create more than 5 wallets. 
Transactions can only be made between wallets with the same currencies. 
If the user makes a transaction between his wallets, then the commission is not charged. 
If the transaction is to the wallet of another user, then the commission is 10%
<br>
<br>
#### Stack: Python, Django, DRF, Django ORM, PostgreSQL



### Dependencies:


<table>
    <tr>
        <th>python</th>
        <th>^3.9</th>
    </tr>
    <tr>
        <th>django</th>
        <th>^4.1.7</th>
    </tr>
    <tr>
        <th>djangorestframework</th>
        <th>^3.14.0</th>
    </tr>
    <tr>
        <th>psycopg2</th>
        <th>^2.9.5</th>
    </tr>
    <tr>
        <th>djangorestframework-simplejwt</th>
        <th>^5.2.2</th>
    </tr>
</table>

### MAKE file:
<table>
    <tr>
        <th>make install</th>
        <th>Install all required dependencies</th>
    </tr>
    <tr>
        <th>make mm</th>
        <th>^4.1.7</th>
    </tr>
</table>

<br>

### Data Base instructions:
1. Connect to PostgreSQL: <br>
sudo postgres psql <br>
 <br>
2. Create DB:<br>
CREATE DATABASE drf_project2;<br>
 <br>
3. Create user & set password:<br>
CREATE USER djangouser WITH PASSWORD 'password';<br>
 <br>
4. Set encoding UTF-8:<br>
ALTER ROLE djangouser SET client_encoding TO 'utf8';<br>
 <br>
5. Set isolation level: <br>
ALTER ROLE djangouser SET default_transaction_isolation TO 'read committed';<br>
 <br>
6. Set time zone UTC: <br>
ALTER ROLE djangouser SET timezone TO 'UTC';<br>
 <br>
7. Grant permissions for user: <br>
GRANT ALL PRIVILEGES ON DATABASE drf_project2 TO djangouser;<br>
 <br>
8. Set environment variables in .env

<br>


### URLS:

User registration: <br>
/autn/register/

Getting token: <br>
/autn/token/

Wallet creation: <br>
POST /wallet/

Displaying all wallets for the current user: <br>
GET /wallets/

Retrieve wallet details: <br>
GET /wallets/<wallet_name>

Delete wallet: <br>
DELETE /wallets/<wallet_name>

Creating transaction: <br>
POST /wallets/transactions/

Get all transactions for current user: <br>
GET /wallets/transactions/

Retrieve transaction details: <br>
GET /wallets/transactions/<transaction_id>

Get all transactions where wallet was sender or receiver: <br>
GET /wallets/transactions/<wallet_name> 
