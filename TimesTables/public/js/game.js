/*
Multiple choice table in an app. 
2x12, each array input numbers


Answer:
	 1 2 3 4    Ans.
	 _ _ _ _
1	|_|_|_|_|	1 2 3 4
2	|_|_|_|_|   2 4 6 8
3	|_|_|_|_|   3 6 9 12
4	|_|_|_|_|   4 8 12 16
5	|_|_|_|_|   5 10 15 20
6	|_|_|_|_|   6 12 18 24


User

	 1 2 3 4    
	 _ _ _ _
1	|_|_|_|_|	
2	|_|_|_|_|   
3	|_|_|_|_|   
4	|_|_|_|_|   
5	|_|_|_|_|   
6	|_|_|_|_|   


Marked Grid - Checks if current cell is marked or not

	 1 2 3 4    
	 _ _ _ _
1	|_|_|_|_|	
2	|_|_|_|_|   
3	|_|_|_|_|   
4	|_|_|_|_|   
5	|_|_|_|_|   
6	|_|_|_|_|   


cellCurCursor = (x,y) of where the current cursor is on the cell. 
	Cursor has options to move(LRUP) or click()

	click() action 
		Check if current cell has been previously selected
		If MarkedGrid (cellCurCursor(x,y) ) == false:
		(Continue with algorithm)
			prompt user for input 
			Listen for user input
			Check if input is equal to the answer grid
			Mark right or wrong in that current grid
			Mark in MarkedGrid that cellCurCursor(x, y) is marked
			Maybe draw in a picture on that cell grid for the User grid to show that it is marked

		If the markedGrid of (cellCurCursor(x,y)) is == true, we cannot use that cell 

	move(direction) action
		4 case switches
		Left - do those actions
		Right -
		Up -
		Down - 


	

	
*/

var questions = ['4 * 3', '5 * 2', '2 * 9', '2 * 0', '4 * 6', '3 * 5', '3 + 4', '12 / 4', '12 + 34', '7*3'];
var solutions = ['12', '10', '18', '0', '24', '15', '7', '3', '46', '21'];
var q_select= 0;
var score = 0;

var start = false;
var startTime = 0;

var previousBlock = "";

// - - - - Owen

/*
Function - ansChecker
@param: xCoor, yCoor, usrInput
@return: True, Fals
-------------------
Description:
Creating 2d ANSWERS table. 5x5 grid
ansChecker function. Take in x and y coordinates and usrInput. 
Return true or false

*/

function ansChecker(xCoor, yCoor, usrInput){
	var answers = {};

	var usrKey = String(xCoor + "," + yCoor);

	for (var y = 0; y < 10; y++){
		for (var x = 0; x < 10; x++){
			var key = String(x + "," + y);
			var value = x*y;
			answers[key] = value;
		}
	}

//Check usrInput with the anser Grid
	if (answers[usrKey] == usrInput){
		console.log("Yay");
		return true;
	} else {
		console.log("Boo!");
		return false;
	}
}

// - - - - Daryl

$(document).keypress(function(e){
	console.log(e.timeStamp);

	//var target = $('#target_input').text();
	var input = $('#attack_input').val();

	if(e.keyCode == '13') {

		if(q_select < (questions.length - 1)){
			console.log('enter hit');
			console.log('solution' + solutions[q_select]);

			if(solutions[q_select] == input && start == true ){
				console.log(score);

				score++;
				q_select++;

				$('#target_input').text(questions[q_select]);
				$('#score').text(score);

				$('#attack_input').val("");	

			} 
			else if(start == true) {
				score--;
				$('#attack_input').val("");	
				$('#score').text(score);
			}

			else if(input == 'start'){
				startTime = e.timeStamp;
				start = true;

				$('#target_input').text(questions[q_select]);
				$('#attack_input').val("");
			}

			if(input == "restart"){
				score = 0;
				q_select = 0;

				alert(q_select);

				startTime = e.timeStamp;
				start = true;

				$('#target_input').text(questions[q_select]);
				$('#attack_input').val("");
			}
		} else {
			var finalTime = e.timeStamp - startTime;
			alert('END' + finalTime);
		}

	}


});

function selectBlock(id) {
	//change back previous block to not selected
	$('#' + previousBlock).removeClass("selected");
	previousBlock = id;
	//Change class to selected
    $('#' + id).addClass("selected");
}
