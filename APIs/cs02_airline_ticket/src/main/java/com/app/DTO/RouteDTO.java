package com.app.DTO;

import javax.validation.constraints.NotNull;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(description = "RouteDTO for Route Creation")
public class RouteDTO {

    @Schema(description = "Name of the Route", required = true)
    @NotNull
    private String name;

    public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Long getDepartureAirportId() {
		return departureAirportId;
	}

	public void setDepartureAirportId(Long departureAirportId) {
		this.departureAirportId = departureAirportId;
	}

	public Long getArrivalAirportId() {
		return arrivalAirportId;
	}

	public void setArrivalAirportId(Long arrivalAirportId) {
		this.arrivalAirportId = arrivalAirportId;
	}

	@Schema(description = "ID of the Departure Airport", required = true)
    @NotNull
    private Long departureAirportId;

    @Schema(description = "ID of the Arrival Airport", required = true)
    @NotNull
    private Long arrivalAirportId;
}

