```
//ENTITY TIPOFORMACION
package com.persona.Backend.Entity.Operational.GestionFormativa;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name = "tipo_formacion")
public class TipoFormacion extends BaseEntity {

	@Column(name = "codigo", length = 10, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "descripcion", length = 60, nullable = false)
	private String descripcion;

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

}
//IREPOSITORY TIPOFORMACION
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.TipoFormacion;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface ITipoFormacionRepository extends IBaseRepository<TipoFormacion, Long> {

}
//ISERVICE TIPOFORMACION
package com.persona.Backend.IService.Operational.GestionFormativa;

import com.persona.Backend.Entity.Operational.GestionFormativa.TipoFormacion;
import com.persona.Backend.IService.IBaseService;

public interface ITipoFormacionService extends IBaseService<TipoFormacion>{

}
//SERVICE TIPOFORMACON
package com.persona.Backend.Service.Operational.GestionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionFormativa.TipoFormacion;
import com.persona.Backend.IService.Operational.GestionFormativa.ITipoFormacionService;
import com.persona.Backend.Service.BaseService;

@Service
public class TipoFormacionService extends BaseService<TipoFormacion> implements ITipoFormacionService{

}
//CONTROLLER TIPOFORMACION 
package com.persona.Backend.Controller.Operational.GestionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionFormativa.TipoFormacion;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_formativa/tipo_formacion")
public class TipoFormacionController extends BaseController<TipoFormacion>{

}

```