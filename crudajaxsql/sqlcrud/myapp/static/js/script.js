$(document).ready(function(){
	$('#success').on('click', function(){
		$name = $('#name').val();
		$mobilenumber = $('#mobilenumber').val();
		$age = $('#age').val();
		$city = $('#city').val();

		if($name == "" || $mobilenumber == "" || $age == "" || $city == ""){
			alert("Please Completed required all fields");
		}
		else{
			$.ajax({
				url: 'create/',
				type: 'POST',
				data:{
					name: $name,
					mobilenumber: $mobilenumber,
					age: $age,
					city: $city,
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
				},
				success:function(response){
					alert("Successfully Added");
				}
			});
		}
	});

	$('.edit').on('click', function(){
		
		$id = $(this).attr('name');
		window.location = "edit/" + $id;
	});

	$('#update').on('click', function(){
		
		$name = $('#name').val();
		$mobilenumber = $('#mobilenumber').val();
		$age = $('#age').val();
		$city = $('#city').val();

		if($name == "" || $mobilenumber == "" || $age == "" || $city == ""){
			alert("Please Complete the required fields");
		}
		else{
			$id = $('#batmen_id').val();
			$.ajax({
				url: 'update/' + $id,
				type: 'POST',
				data: {
					name: $name,
					mobilenumber: $mobilenumber,
					age: $age,
					city: $city,
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
				},
				success:function(response){
					alert("Updated Successfully");
				}

			});
		}
	});

	$('.delete').on('click',function(){

		$id = $(this).attr('name');
		$.ajax({
			
			url: 'delete/' + $id,
			type: 'POST',
			data:{
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success:function(response){
	
			}
		});
           alert("Successfully Deleted");
	});

});