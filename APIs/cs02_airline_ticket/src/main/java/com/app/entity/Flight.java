package com.app.entity;

import java.util.Date;
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
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import javax.validation.constraints.NotNull;

import io.swagger.v3.oas.annotations.media.Schema;
//import io.swagger.annotations.ApiModel;
//import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

@Entity
@Data
@Schema(description = "FlightEntityObject")
public class Flight {
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Schema(description = "Flight_Id")
	private Long id;
	
	@Column(name = "name", length = 50)
	@NotNull
	@Schema(description = "Name_of_Flight", required = true)
	private String name;
	
	@Column(name = "departure_date")
	@Temporal(TemporalType.TIMESTAMP)
	@Schema(description = "Departure_Date_and_Time")
	private Date departureDateTime;
	
	@Column(name = "arrival_date")
	@Temporal(TemporalType.TIMESTAMP)
	@Schema(description = "Arrival_Date_and_Time")
	private Date arrivalDateTime;
	
	@Column(name = "duration")
	@Schema(description = "Flight_Duration")
	private Integer duration;
	
	@Column(name = "quota")
	@Schema(description = "Flight_Quota")
	private Integer quota;
	
	@Column(name = "quota_filled")
	@Schema(description = "Flight_Quota_Filled")
	private Integer quotaFilled;
	
	@Column(name = "quota_filled_percentage")
	@Schema(description = "Flight_Quota_Percentage")
	private Integer quotaFilledPercentage;
	
	@NotNull
	@JoinColumn(name = "route_flight_id")
	//@ManyToOne(fetch = FetchType.LAZY)
	private Long routeID;
	
	@NotNull
	@JoinColumn(name = "route_plane_id")
	//@ManyToOne(fetch = FetchType.LAZY)
	private Long planeID;
	
	
	/*@JoinColumn(name = "flight_company_id")
	@ManyToOne(fetch = FetchType.LAZY)
	private Company company;
	
	@JoinColumn(name = "ticket_flight_id")
	@OneToMany(fetch = FetchType.LAZY)
	private List<Ticket> tickets;*/

	public String getName() {
		// TODO Auto-generated method stub
		return name;
	}

	public Long getId() {
		// TODO Auto-generated method stub
		return id;
	}

	public Integer getQuota() {
		// TODO Auto-generated method stub
		return quota;
	}

	public Integer getQuotaFilled() {
		// TODO Auto-generated method stub
		return quotaFilled;
	}

	public void setQuotaFilled(int i) {
		// TODO Auto-generated method stub
		quotaFilled = i;
	}

	public int getQuotaFilledPercentage() {
		// TODO Auto-generated method stub
		return quotaFilledPercentage;
	}

	public void setQuotaFilledPercentage(int i) {
		// TODO Auto-generated method stub
		quotaFilledPercentage = i;
	}

}
