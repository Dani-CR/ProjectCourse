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

import com.app.DTO.FlightDTO;
import com.app.entity.Flight;
import com.app.entity.Plane;
import com.app.entity.Route;
import com.app.service.impl.FlightServiceImpl;
import com.app.service.impl.PlaneServiceImpl;
import com.app.service.impl.RouteServiceImpl;
import com.app.util.ApiPaths;

//import io.swagger.annotations.ApiOperation;
import io.swagger.v3.oas.annotations.Operation;

@RestController
@RequestMapping(ApiPaths.FlightCtrl.PATH)
public class FlightController {

    @Autowired
    FlightServiceImpl flightServiceImpl;

    @Autowired
    private PlaneServiceImpl planeServiceImpl;

    @Autowired
    private RouteServiceImpl routeServiceImpl;

    @PostMapping
    @Operation(description = "Create a new Flight")
    public ResponseEntity<?> create(@Valid @RequestBody FlightDTO flightDTO) {
        // Check if a flight with the same name already exists
        if (flightServiceImpl.getByName(flightDTO.getName()) != null) {
            return new ResponseEntity<>("Flight with this name already exists", HttpStatus.CONFLICT);
        }

        // Fetch the Plane and Route entities
        Plane plane = planeServiceImpl.getById(flightDTO.getPlaneId());
        Route route = routeServiceImpl.getById(flightDTO.getRouteId());
        if (plane == null) {
	        return new ResponseEntity<>("plane not found", HttpStatus.NOT_FOUND);
	    }
        if (route == null) {
	        return new ResponseEntity<>("route not found", HttpStatus.NOT_FOUND);
	    }

        // Map DTO to Flight entity
        Flight flight = new Flight();
        flight.setName(flightDTO.getName());
        flight.setDepartureDateTime(flightDTO.getDepartureDateTime());
        flight.setArrivalDateTime(flightDTO.getArrivalDateTime());
        flight.setDuration(flightDTO.getDuration());
        flight.setQuota(flightDTO.getQuota());
        flight.setPlane(plane);
        flight.setRoute(route);

        // Save the Flight
        flight = flightServiceImpl.save(flight);
        return new ResponseEntity<>(flight, HttpStatus.CREATED);
    }
	@GetMapping("/{id}")
	@Operation(description = "Get By Id Operation")//, response = Flight.class)
	public ResponseEntity<?> getById(@PathVariable(value = "id", required = true) Long id) {
		Flight flight = flightServiceImpl.getById(id);
		return new ResponseEntity<>(flight, HttpStatus.OK);
	}

	@DeleteMapping("/{id}")
	@Operation(description = "Delete Operation")
	public ResponseEntity<?> delete(@PathVariable(value = "id", required = true) Long id) {
		flightServiceImpl.delete(id);
		return new ResponseEntity<>(HttpStatus.OK);
	}

	@PutMapping
	@Operation(description = "Update Operation")//, response = Flight.class)
	public ResponseEntity<?> update(@Valid @RequestBody Flight flight) {

		flight = flightServiceImpl.update(flight);
		return new ResponseEntity<>(flight, HttpStatus.OK);
	}

	@GetMapping
	@Operation(description = "Get All Operation")//, response = Flight.class, responseContainer = "List")
	public ResponseEntity<?> getAll() {
		List<Flight> flightList = flightServiceImpl.getAll();
		return new ResponseEntity<>(flightList, HttpStatus.OK);
	}

}
