package com.app.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.validation.constraints.NotNull;

//import io.swagger.annotations.ApiModel;
//import io.swagger.annotations.ApiModelProperty;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Entity
@Data
@Schema(description = "PlaneEntityObject")
public class Plane {
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Schema(description = "Plane_Id")
	private Long id;
	
	@Column(name = "name", length = 20)
	@NotNull
	@Schema(description = "Name_of_Plane", required = true)
	private String name;
	
	@Column(name = "number_seat")
	@Schema(description = "Number_Of_Seats")
	private Integer numberOfSeats;
	
	@JoinColumn(name = "company_plane_id")
	private Long companyID;

	public String getName() {
		// TODO Auto-generated method stub
		return name;
	}

}
