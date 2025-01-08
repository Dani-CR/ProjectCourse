package com.app.controller;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.app.DTO.RouteDTO;
import com.app.entity.Airport;
import com.app.entity.Route;
import com.app.service.impl.AirportServiceImpl;
import com.app.service.impl.RouteServiceImpl;
import com.app.util.ApiPaths;

import io.swagger.v3.oas.annotations.Operation;

//import io.swagger.annotations.ApiOperation;

@RestController
@RequestMapping(ApiPaths.RouteCtrl.PATH)
public class RouteController {

	@Autowired
	RouteServiceImpl routeServiceImpl;
	
	@Autowired
	private AirportServiceImpl airportServiceImpl;

	@PostMapping
	@Operation(description = "Create Operation")//, response = Route.class)
	public ResponseEntity<?> create(@Valid @RequestBody RouteDTO routeDTO) {
	        // Check if a route with the same name already exists
	        if (routeServiceImpl.getByName(routeDTO.getName()) != null) {
	            return new ResponseEntity<>("Route with this name already exists", HttpStatus.CONFLICT);
	        }

	        // Fetch the Departure and Arrival Airports
	        Airport departureAirport = airportServiceImpl.getById(routeDTO.getDepartureAirportId());
	        Airport arrivalAirport = airportServiceImpl.getById(routeDTO.getArrivalAirportId());
	        
	        if (departureAirport == null) {
		        return new ResponseEntity<>("depart. airport not found", HttpStatus.NOT_FOUND);
		    }
	        
	        if (arrivalAirport == null) {
		        return new ResponseEntity<>("arrival airport not found", HttpStatus.NOT_FOUND);
		    }
	        
	        if (departureAirport.getName() == arrivalAirport.getName()) {
		        return new ResponseEntity<>("Depart. and arrival can not be the same", HttpStatus.CONFLICT);
		    }

	        // Map DTO to Route entity
	        Route route = new Route();
	        route.setName(routeDTO.getName());
	        route.setDepartureAirport(departureAirport);
	        route.setArrivalAirport(arrivalAirport);

	        // Save the Route
	        route = routeServiceImpl.save(route);
	        return new ResponseEntity<>(route, HttpStatus.CREATED);
	}

	@GetMapping("/{id}")
	@Operation(description = "Get By Id Operation")//, response = Route.class)
	public ResponseEntity<?> getById(@PathVariable(value = "id", required = true) Long id) {
		Route route = routeServiceImpl.getById(id);
		return new ResponseEntity<>(route, HttpStatus.OK);
	}

	@DeleteMapping("/{id}")
	@Operation(description = "Delete Operation")
	public ResponseEntity<?> delete(@PathVariable(value = "id", required = true) Long id) {
		routeServiceImpl.delete(id);
		return new ResponseEntity<>(HttpStatus.OK);
	}

	@PutMapping
	@Operation(description = "Update Operation")//, response = Route.class)
	public ResponseEntity<?> update(@Valid @RequestBody Route route) {

		route = routeServiceImpl.update(route);
		return new ResponseEntity<>(route, HttpStatus.OK);
	}

	@GetMapping
	@Operation(description = "Get All Operation")//, response = Route.class, responseContainer = "List")
	public ResponseEntity<?> getAll() {
		List<Route> routeList = routeServiceImpl.getAll();
		return new ResponseEntity<>(routeList, HttpStatus.OK);
	}

}
