package com.app.DTO;

import java.util.Date;

import javax.validation.constraints.NotNull;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(description = "FlightDTO for Flight Creation")
public class FlightDTO {

    @Schema(description = "Name of the Flight", required = true)
    @NotNull
    private String name;

    public Date getDepartureDateTime() {
		return departureDateTime;
	}

	public void setDepartureDateTime(Date departureDateTime) {
		this.departureDateTime = departureDateTime;
	}

	public Date getArrivalDateTime() {
		return arrivalDateTime;
	}

	public void setArrivalDateTime(Date arrivalDateTime) {
		this.arrivalDateTime = arrivalDateTime;
	}

	public Integer getDuration() {
		return duration;
	}

	public void setDuration(Integer duration) {
		this.duration = duration;
	}

	public Integer getQuota() {
		return quota;
	}

	public void setQuota(Integer quota) {
		this.quota = quota;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Long getPlaneId() {
		return planeId;
	}

	public void setPlaneId(Long planeId) {
		this.planeId = planeId;
	}

	public Long getRouteId() {
		return routeId;
	}

	public void setRouteId(Long routeId) {
		this.routeId = routeId;
	}

	@Schema(description = "Departure Date and Time", example = "2024-12-25T10:30:00")
    private Date departureDateTime;

    @Schema(description = "Arrival Date and Time", example = "2024-12-25T14:30:00")
    private Date arrivalDateTime;

    @Schema(description = "Flight Duration in Minutes")
    private Integer duration;

    @Schema(description = "Flight Quota")
    private Integer quota;

    @Schema(description = "ID of the Plane", required = true)
    @NotNull
    private Long planeId;

    @Schema(description = "ID of the Route", required = true)
    @NotNull
    private Long routeId;
}

