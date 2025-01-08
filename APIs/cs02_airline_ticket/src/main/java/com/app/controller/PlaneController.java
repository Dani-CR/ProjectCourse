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

import com.app.DTO.PlaneDTO;
import com.app.entity.Company;
import com.app.entity.Plane;
import com.app.service.impl.CompanyServiceImpl;
import com.app.service.impl.PlaneServiceImpl;
import com.app.util.ApiPaths;

//import io.swagger.annotations.ApiOperation;
import io.swagger.v3.oas.annotations.Operation;

@RestController
@RequestMapping(ApiPaths.PlaneCtrl.PATH)
public class PlaneController {

	@Autowired
	PlaneServiceImpl planeServiceImpl;
	@Autowired
	CompanyServiceImpl companyServiceImpl;

	@PostMapping
	@Operation(description = "Create Operation")//, response = Plane.class)
	public ResponseEntity<?> create(@Valid @RequestBody PlaneDTO planeDTO) {
	    if (planeServiceImpl.getByName(planeDTO.getName()) != null) {
	        return new ResponseEntity<>(HttpStatus.CONFLICT);
	    }

	    // Convert PlaneDTO to Plane entity
	    Plane plane = new Plane();
	    plane.setName(planeDTO.getName());
	    plane.setNumberOfSeats(planeDTO.getNumberOfSeats());

	    // Find the company by ID and set it in the Plane entity
	    Company company = companyServiceImpl.getById(planeDTO.getCompanyId());
	    if (company == null) {
	        return new ResponseEntity<>("Company not found", HttpStatus.NOT_FOUND);
	    }
	    plane.setCompany(company);

	    // Save the Plane entity
	    plane = planeServiceImpl.save(plane);
	    return new ResponseEntity<>(plane, HttpStatus.CREATED);
	}

	@GetMapping("/{id}")
	@Operation(description = "Get By Id Operation")//, response = Plane.class)
	public ResponseEntity<?> getById(@PathVariable(value = "id", required = true) Long id) {
		Plane plane = planeServiceImpl.getById(id);
		return new ResponseEntity<>(plane, HttpStatus.OK);
	}

	@DeleteMapping("/{id}")
	@Operation(description = "Delete Operation")
	public ResponseEntity<?> delete(@PathVariable(value = "id", required = true) Long id) {
		planeServiceImpl.delete(id);
		return new ResponseEntity<>(HttpStatus.OK);
	}

	@PutMapping
	@Operation(description = "Update Operation")//, response = Plane.class)
	public ResponseEntity<?> update(@Valid @RequestBody Plane plane) {

		plane = planeServiceImpl.update(plane);
		return new ResponseEntity<>(plane, HttpStatus.OK);
	}

	@GetMapping
	@Operation(description = "Get All Operation")//, response = Plane.class, responseContainer = "List")
	public ResponseEntity<?> getAll() {
		List<Plane> planeList = planeServiceImpl.getAll();
		return new ResponseEntity<>(planeList, HttpStatus.OK);
	}

}
