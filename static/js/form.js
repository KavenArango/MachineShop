$(document).ready(function(){

    $('form').on('submit',function (event) {

        $.ajax({
            data:{
                blockId:            $('#blockId').val(),
                User_ID:            $('#User_ID').val(),
                Machine_ID:         $('#Machine_ID').val(),
                MachineBookingTime: $('#MachineBookingTime').val(),
                MachineBookingDate: $('#MachineBookingDate').val(),
                DateMachineBooked:  $('#DateMachineBooked').val(),
          },
			type : 'POST',
			url : '/process',
		});
		event.preventDefault();
	});
});