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

import com.app.DTO.TicketDTO;
import com.app.entity.Flight;
import com.app.entity.Ticket;
import com.app.service.impl.FlightServiceImpl;
import com.app.service.impl.TicketServiceImpl;
import com.app.util.ApiPaths;

import io.swagger.v3.oas.annotations.Operation;

//import io.swagger.annotations.ApiOperation;

@RestController
@RequestMapping(ApiPaths.TicketCtrl.PATH)
public class TicketController {

	@Autowired
	TicketServiceImpl ticketServiceImpl;
	@Autowired
	private FlightServiceImpl flightServiceImpl;

	@PostMapping
	@Operation(description = "Create Operation")//, response = Ticket.class)
	public ResponseEntity<?> create(@Valid @RequestBody TicketDTO ticketDTO) {
		// Check if a ticket with the same code already exists
        if (ticketServiceImpl.getByCode(ticketDTO.getTicketCode()) != null) {
            return new ResponseEntity<>("Ticket with this code already exists", HttpStatus.CONFLICT);
        }

        // Fetch the Flight entity
        Flight flight = flightServiceImpl.getById(ticketDTO.getFlightId());

        // Map DTO to Ticket entity
        Ticket ticket = new Ticket();
        ticket.setTicketCode(ticketDTO.getTicketCode());
        ticket.setPrice(ticketDTO.getPrice());
        ticket.setIsSold(ticketDTO.getIsSold());
        ticket.setFlight(flight);

        // Save the Ticket
        ticket = ticketServiceImpl.save(ticket);
        return new ResponseEntity<>(ticket, HttpStatus.CREATED);
	}

	@GetMapping("/{id}")
	@Operation(description = "Get By Id Operation")//, response = Ticket.class)
	public ResponseEntity<?> getById(@PathVariable(value = "id", required = true) Long id) {
		Ticket ticket = ticketServiceImpl.getById(id);
		return new ResponseEntity<>(ticket, HttpStatus.OK);
	}

	@DeleteMapping("/{id}")
	@Operation(description = "Delete Operation")
	public ResponseEntity<?> delete(@PathVariable(value = "id", required = true) Long id) {
		ticketServiceImpl.delete(id);
		return new ResponseEntity<>(HttpStatus.OK);
	}

	@PutMapping
	@Operation(description = "Update Operation")//, response = Ticket.class)
	public ResponseEntity<?> update(@Valid @RequestBody Ticket ticket) {
		ticket = ticketServiceImpl.update(ticket);
		return new ResponseEntity<>(ticket, HttpStatus.OK);
	}

	@GetMapping
	@Operation(description = "Get All Operation")//, response = Ticket.class, responseContainer = "List")
	public ResponseEntity<?> getAll() {
		List<Ticket> ticketList = ticketServiceImpl.getAll();
		return new ResponseEntity<>(ticketList, HttpStatus.OK);
	}

}
