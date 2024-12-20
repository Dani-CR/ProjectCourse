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

import io.swagger.v3.oas.annotations.media.Schema;
//import io.swagger.annotations.ApiModel;
//import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

@Entity
@Data
@Schema(description = "CompanyEntityObject")
public class Company {
	
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	@Column(name="id")
	@Schema(description = "Company_Id")
	private Long id;
	
	@Column(name = "name", length = 50)
	@Schema(description = "Name_Of_Company", required = true)
	private String name;
	
    /*@JoinColumn(name = "company_plane_id")
    @OneToMany(fetch = FetchType.LAZY)
    private List<Plane> planes;
    
    @JoinColumn(name = "flight_company_id")
    @OneToMany(fetch = FetchType.LAZY)
    private List<Flight> flights;*/
	
    public String getName() {
    	return name;
    }

}
