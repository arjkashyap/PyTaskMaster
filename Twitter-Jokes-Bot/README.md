<h3>Python bot for posting Dirty jokes on twitter everyday at 10</h3>
<br/>
<h5> Requirements: </h5>
	<ol>
		<li>  Python3.6 </li>
		<li> Twitter Handle </li>
		<li> Internet Connection</li>
	</ol>
</p>

<tr/>

<h5> Dependencies: </h5>
	<p> Install the following dependencies using pip3</p>
	<ol>
		<li>  Bs4 </li>
		<li> lxml </li>
		<li> urllib</li>
		<li> Selenium </li>
	</ol>
<tr/>
<h5> Setup</h5>

<p>
	You need to create a file named config.py in the root dir.
	add the following lines in it:
</p>

	username: "yourtwitterusername"
	pswd: "yourpassword"
	
	denied = []  # Enter the list of words which will serve as a parameter to filter out Offensive tweets 
		

<p> Finnaly run publish.py. </p>

