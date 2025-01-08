package com.app.DTO;

import javax.validation.constraints.NotNull;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(description = "TicketDTO for Ticket Creation")
public class TicketDTO {

    @Schema(description = "Code of the Ticket", required = true)
    @NotNull
    private String ticketCode;

    @Schema(description = "Price of the Ticket")
    private Integer price;

    @Schema(description = "Is the Ticket Sold?")
    private Boolean isSold;

    @Schema(description = "ID of the Flight", required = true)
    @NotNull
    private Long flightId;

	public String getTicketCode() {
		return ticketCode;
	}

	public void setTicketCode(String ticketCode) {
		this.ticketCode = ticketCode;
	}

	public Integer getPrice() {
		return price;
	}

	public void setPrice(Integer price) {
		this.price = price;
	}

	public Boolean getIsSold() {
		return isSold;
	}

	public void setIsSold(Boolean isSold) {
		this.isSold = isSold;
	}

	public Long getFlightId() {
		return flightId;
	}

	public void setFlightId(Long flightId) {
		this.flightId = flightId;
	}
}

