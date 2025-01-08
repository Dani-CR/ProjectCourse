package com.app.entity;

import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;

//import io.swagger.annotations.ApiModel;
//import io.swagger.annotations.ApiModelProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Entity
@Data
@Schema(description = "RouteEntityObject")
public class Route {
	@Column(name = "id")
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Schema(description = "Route_Id")
	private Long id;
	
	@Column(name="name", length= 50)
	@Schema(description = "Name_of_Route", required = true)
	private String name;
	
	@JoinColumn(name = "departure_airport_id")
	@ManyToOne(fetch = FetchType.LAZY)
	private Airport departureAirport;
	
	@JoinColumn(name = "arrival_airport_id")
	@ManyToOne(fetch = FetchType.LAZY)
	private Airport arrivalAirport;	
	
	/*@JoinColumn(name = "route_flight_id")
	@OneToMany(fetch = FetchType.LAZY)
	private List<Flight> flights;*/

	public Airport getDepartureAirport() {
		return departureAirport;
	}

	public void setDepartureAirport(Airport departureAirport) {
		this.departureAirport = departureAirport;
	}

	public Airport getArrivalAirport() {
		return arrivalAirport;
	}

	public void setArrivalAirport(Airport arrivalAirport) {
		this.arrivalAirport = arrivalAirport;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getName() {
		// TODO Auto-generated method stub
		return name;
	}


}
