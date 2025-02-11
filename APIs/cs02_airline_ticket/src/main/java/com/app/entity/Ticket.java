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
@Schema(description = "TicketEntityObject")
public class Ticket {
	@Column(name = "id")
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Schema(description = "Ticket_Id")
	private Long id;
	
	@Column(name = "ticket_code")
	@NotNull
	@Schema(description = "Code_of_Ticket", required = true)
	private String ticketCode;
	
	@JoinColumn(name = "flight_ticket_id")
	@ManyToOne(fetch = FetchType.LAZY)
	private Flight flight;
	
	@Column(name = "price")
	@Schema(description = "Price_of_Ticket")
	private Integer price;
	
	@Column(name = "is_sold")
	@Schema(description = "Is_Ticket_Sold")
	private Boolean isSold; //   0: Cancelled, 1: Sold
	
	public void setTicketCode(String ticketCode) {
		this.ticketCode = ticketCode;
	}

	public void setFlight(Flight flight) {
		this.flight = flight;
	}

	public void setPrice(Integer price) {
		this.price = price;
	}

	public void setIsSold(Boolean isSold) {
		this.isSold = isSold;
	}

	public String getTicketCode() {
		// TODO Auto-generated method stub
		return ticketCode;
	}

	public boolean getIsSold() {
		// TODO Auto-generated method stub
		return isSold;
	}

	public Flight getFlight() {
		// TODO Auto-generated method stub
		return flight;
	}

	public int getPrice() {
		// TODO Auto-generated method stub
		return price;
	}

	public void setPrice(int newPrice) {
		// TODO Auto-generated method stub
		price = newPrice;
	}
	
}
