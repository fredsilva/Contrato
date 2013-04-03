<?php

	$year = date('Y');
	$month = date('m');
        $day = date('d');      
        $dataConsulta = $day+2;

	echo json_encode(array(
	
		array(
			'id' => 111,
			'title' => 'Consulta Frederico',
			'start' => "$year-$month-$dataConsulta"			
		),
		
		array(
			'id' => 222,
			'title' => 'Consulta Mara',
			'start' => "$year-$month-20",
			'end' => "$year-$month-22",
			'url' => 'http://yahoo.com/'
		)
	
	));

?>
