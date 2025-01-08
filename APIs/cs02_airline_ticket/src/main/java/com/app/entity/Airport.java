package com.app.entity;

import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToMany;
import javax.validation.constraints.NotNull;

//import io.swagger.annotations.ApiModel;
//import io.swagger.annotations.ApiModelProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Entity
@Data
@Schema(description = "AirportEntityObject")
public class Airport {
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Column(name = "id")
	@Schema(description = "Airport Id")
	private Long id;
	
	@Column(name = "name", length = 50)
	@NotNull
	@Schema(description = "Name of Airport", required = true)
	private String name;	
	
	@Column(name = "capacity")
	@Schema(description = "Capacity of Airport")
	private Integer capacity;
	
	@Column(name = "location", length = 100)
	@Schema(description = "Location of Airport")
	private String location;
	
	/*@JoinColumn(name = "departure_airport_id")
	@OneToMany//(fetch = FetchType.LAZY)
	private List<Route> departureRoutes;
	
	@JoinColumn(name = "arrival_airport_id")
	@OneToMany//(fetch = FetchType.LAZY)
	private List<Route> arrivalRoutes;*/

	public String getName() {
		// TODO Auto-generated method stub
		return name;
	}

}
