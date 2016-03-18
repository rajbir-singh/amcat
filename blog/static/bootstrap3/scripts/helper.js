var ausi = toString("{% \'static/img/%data%.png\' %}");
var skills = '<div class="col-md-3"><img src="%x%" alt="my skills" class="img-responsive img-circle"></div>';
skills.replace('%x%', ausi);
var skills_array = ['c++', 'python', 'php', 'java'];

var skills_new = '';

for(var i=0; i < skills_array.length; i += 1){
skills_new = skills.replace('%data%', skills_array[i]);
$('.skills-section-images').append(skills_new);
}

var project = '<li><h4 class="text-uppercase">%project%  <p class="year">(%year%) </p> </h4> <p>%details%</p></li><hr>';
				
var project_array=[
{
	project:'cooltree.herokuapp.com (Group project : 3 members)',
	year:'2015',
	details:'cooltree is a website, designed on the lines of popular social networking sites like facebook and twitter to facilitate interaction among registered users.Registered users can interact with each other by live chat, or could write their blog, website includes features like login system, safety from sql injection, personal details and photos upload.Amongst the team members i had the responsibility of handling the back-end of the system.Used php, Mysqli.'
},
{
	project:'Stock Chart Analyser',
	year:'2015',
	details:'developed a python script which predicts future performance of stocks.The script pulls stock data from Yahoo Finacance API, plots it on a timeline along with different moving averages.The comparison between the averages allows to analyse the performance of the stock in recent past thus one gets a hint about the momentum in a stock\'s trade.Prediction process also involves computing RSI (Relative Strength Index) which indicates if a stock is overbought or oversold in comparison to its actual evaluation.'
},
{
	project:'Real Estate Portal',
	year:'2014',
	details:'Designed a website, which allowed to buy, sell, rent property online by the registered users.You just need to be a registered user to start trading in Real Estate.Keyfeatures like login system, safety from sql injection, sending e-mail.Used HTML/CSS, php, Mysqli.'
},
{
	project:'Data Analytics',
	year:'2014',
	details:'Implemented Machine Learning algorithms like Gradient Descent, Linear Regression, Logistic Regression, Neural Networks in python.'
},
{
	project:'Data Encryption Standard (Group project : 3 members)',
	year:'2013',
	details:'DES is a symmetric key algorithm for the encryption of electronic data.Soon after it\'s launch in late \'80s it became a standard algorithm for the purpose of encryption across the globe.As the time passed computing power increased more sophisticated Encrypting algorithms like AES were introduced. Amongst the team members I handled implementation of the algorithm using Java.'
}
]

var project_new = '';
for(var i=0; i < project_array.length; i +=1)
{
	project_new = project.replace('%project%', project_array[i]['project']);
	project_new = project_new.replace('%year%', project_array[i]['year']);
	project_new = project_new.replace('%details%', project_array[i]['details']);
	$('.projects-section').append(project_new);
}

var loggedIn=false;
	$(document).ready(function () {
		$('#btn').on('click', function(){
			$('#content').slideDown();
			});

	$('#btnLogin').on('click', function() {
	//alert('hello');
		$('#login').slideDown();
	});

		$('#btnSubmit').on('click', function() {
		$('#log').slideDown();
	});

	$(document).on('submit', '#new_form', function(e){
		e.preventDefault();

		$.ajax({
			type:'POST',
			url:'/blog/create/',
			data:{
				name:$('#name').val(),
				email:$('#email').val(),
				title:$('#title').val(),
				data:$('#data').val(),
				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
			},
			success:function(){
				alert('done!! thanks for your comment');
				location.reload(true);
			}
		});
	});

	});