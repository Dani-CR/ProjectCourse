package com.app.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import io.swagger.v3.oas.models.media.Schema;
import org.springdoc.core.customizers.OpenApiCustomiser;
import org.springdoc.core.*;

@Configuration
public class SwaggerConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("Issue Management API Reference")
                        .version("1.0.0")
                        .description("API documentation for Issue Management system"));
    }

    @Bean
    public OpenApiCustomiser customSchemaMapping() {
        return openApi -> {
            // Replace LocalDate with String in schema
            openApi.getComponents().addSchemas("LocalDate", new Schema<>().type("string").example("2024-12-14"));
        };
    }

    @Bean
    public GroupedOpenApi apiGroup() {
        return GroupedOpenApi.builder()
                .group("default")
                .pathsToMatch("/**") // Equivalent to PathSelectors.any()
                .packagesToScan("com.app") // Equivalent to RequestHandlerSelectors.basePackage("com.app")
                .build();
    }
}



/*import java.time.LocalDate;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.ResponseEntity;

import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;


@Configuration
@EnableSwagger2
public class SwaggerConfig {

    ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("Issue Management API Reference")
                .version("1.0.0")
                .build();
    }

    @Bean
    public Docket customImplementation() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .select().paths(PathSelectors.any())
                .apis(RequestHandlerSelectors.basePackage("com.app"))
                .build()
                .pathMapping("/")
                .useDefaultResponseMessages(false)
                .directModelSubstitute(LocalDate.class, String.class)
                .genericModelSubstitutes(ResponseEntity.class);
    }
}*/