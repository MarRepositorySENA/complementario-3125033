```
//ENTIDAD PERSONA 

package com.persona.Backend.Entity.Security;

import java.time.LocalDate;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Enum.TipoDocumento;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "persona")
public class Persona extends BaseEntity {

	@Column(name = "primer_nombre", length = 45, nullable = false)
	private String primerNombre;

	@Column(name = "segundo_nombre", length = 45)
	private String segundoNombre;

	@Column(name = "primer_apellido", length = 45, nullable = false)
	private String primerApellido;

	@Column(name = "segundo_apellido", length = 45)
	private String segundoApellido;

	@Column(name = "tipo_documento", nullable = false)
	private String tipoDocumento;

	@Column(name = "numero_documento", nullable = false)
	private String numeroDocumento;

	@Column(name = "email")
	private String email;

	@Column(name = "genero")
	private String genero;

	@Column(name = "direccion")
	private String direccion;

	@Column(name = "telefono")
	private String telefono;

	@Column(name = "fecha_nacimiento")
	private LocalDate fechaNacimiento;

	public String getPrimerNombre() {
		return primerNombre;
	}

	public void setPrimerNombre(String primerNombre) {
		this.primerNombre = primerNombre;
	}

	public String getSegundoNombre() {
		return segundoNombre;
	}

	public void setSegundoNombre(String segundoNombre) {
		this.segundoNombre = segundoNombre;
	}

	public String getPrimerApellido() {
		return primerApellido;
	}

	public void setPrimerApellido(String primerApellido) {
		this.primerApellido = primerApellido;
	}

	public String getSegundoApellido() {
		return segundoApellido;
	}

	public void setSegundoApellido(String segundoApellido) {
		this.segundoApellido = segundoApellido;
	}

	
	public String getTipoDocumento() {
		return tipoDocumento;
	}

	public void setTipoDocumento(String tipoDocumento) {
		this.tipoDocumento = tipoDocumento;
	}

	public String getNumeroDocumento() {
		return numeroDocumento;
	}

	public void setNumeroDocumento(String numeroDocumento) {
		this.numeroDocumento = numeroDocumento;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getGenero() {
		return genero;
	}

	public void setGenero(String genero) {
		this.genero = genero;
	}

	public String getDireccion() {
		return direccion;
	}

	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}

	public String getTelefono() {
		return telefono;
	}

	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}

	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}

	public void setFechaNacimiento(LocalDate fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}

}
//IREPOSITORY PERSONA
package com.persona.Backend.IRepository.Security;


import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Security.Persona;
import com.persona.Backend.IRepository.IBaseRepository;


@Repository
public interface IPersonaRepository extends IBaseRepository<Persona, Long>{

	
}
//ISERVICE PERSONA

package com.persona.Backend.IService.Security;

import com.persona.Backend.Entity.Security.Persona;
import com.persona.Backend.IService.IBaseService;

public interface IPersonaService extends IBaseService<Persona>{

}
//SERVICE PERSONA

package com.persona.Backend.Service.Security;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Security.Persona;
import com.persona.Backend.IService.Security.IPersonaService;
import com.persona.Backend.Service.BaseService;

@Service
public class PersonaService extends BaseService<Persona> implements IPersonaService {
	
	

}
//CONTROLLER PERSONA
package com.persona.Backend.Controller.Security;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Security.Persona;



@CrossOrigin("*")//permite que cualquier dominio tenga acceso a el
@RestController
@RequestMapping("/api/v1/base/security/persona")
public class PersonaController  extends BaseController<Persona>{

	

}


```
