package com.app.DTO;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;

@Data
@Schema(description = "PlaneDataTransferObject for Plane Creation")
public class PlaneDTO {

    @Schema(description = "Name of the Plane", required = true, example = "Boeing 747")
    private String name;

    @Schema(description = "Number of Seats in the Plane", example = "300")
    private Integer numberOfSeats;

    @Schema(description = "ID of the Company owning the Plane", required = true, example = "1")
    private Long companyId;

    // Getters and Setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getNumberOfSeats() {
        return numberOfSeats;
    }

    public void setNumberOfSeats(Integer numberOfSeats) {
        this.numberOfSeats = numberOfSeats;
    }

    public Long getCompanyId() {
        return companyId;
    }

    public void setCompanyId(Long companyId) {
        this.companyId = companyId;
    }
}
